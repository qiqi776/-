"""验证项目拼装包生成器能一次输出选型、组件清单、风险报告、架构图、执行清单、Issue 草案和标签配置。"""

import json
import shutil
import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "generate_project_package.py"


class GenerateProjectPackageTests(unittest.TestCase):
    def setUp(self):
        # 构造最小组件索引，覆盖主组件、备选组件和高接入成本风险。
        self.components = [
            {
                "name": "FastAPI",
                "category": "backend",
                "github": "https://github.com/fastapi/fastapi",
                "website": "https://fastapi.tiangolo.com",
                "module": "后端 / API",
                "license": "MIT",
                "integration_cost": "低",
                "score": "5/5",
                "notes": "适合快速构建 API。",
                "avoid_when": "需要完整全栈框架。",
            },
            {
                "name": "NestJS",
                "category": "backend",
                "github": "https://github.com/nestjs/nest",
                "website": "https://nestjs.com",
                "module": "后端 / API",
                "license": "MIT",
                "integration_cost": "中",
                "score": "4/5",
                "notes": "适合 TypeScript 团队。",
                "avoid_when": "团队主要使用 Python。",
            },
            {
                "name": "Keycloak",
                "category": "auth",
                "github": "https://github.com/keycloak/keycloak",
                "website": "https://www.keycloak.org",
                "module": "认证 / IAM",
                "license": "Apache-2.0",
                "integration_cost": "高",
                "score": "4/5",
                "notes": "适合企业身份。",
                "avoid_when": "只需要轻量登录。",
            },
        ]

    def test_cli_generates_project_assembly_package(self):
        # 验证命令行能把一个项目的选型清单、组件清单和风险报告写入同一目录。
        tmp_dir = ROOT / "tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_index = tmp_dir / "project-package-index.json"
        output_dir = tmp_dir / "project-package"
        if output_dir.exists():
            shutil.rmtree(output_dir)
        tmp_index.write_text(
            json.dumps({"component_count": len(self.components), "components": self.components}, ensure_ascii=False),
            encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--index",
                str(tmp_index),
                "--modules",
                "backend,auth",
                "--project-name",
                "后台示例",
                "--output-dir",
                str(output_dir),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("已生成项目拼装包", result.stdout)
        self.assertTrue((output_dir / "README.md").exists())
        self.assertTrue((output_dir / "stack-plan.json").exists())
        self.assertTrue((output_dir / "component-manifest.md").exists())
        self.assertTrue((output_dir / "risk-check.md").exists())
        self.assertTrue((output_dir / "integration-plan.md").exists())
        self.assertTrue((output_dir / "architecture-map.md").exists())
        self.assertTrue((output_dir / "assembly-checklist.md").exists())
        self.assertTrue((output_dir / ".env.example").exists())
        self.assertTrue((output_dir / "PROJECT-README.md").exists())
        self.assertTrue((output_dir / "github-issues.md").exists())
        self.assertTrue((output_dir / "github-labels.json").exists())

        stack_plan = json.loads((output_dir / "stack-plan.json").read_text(encoding="utf-8"))
        self.assertEqual(stack_plan["modules"][0]["primary"]["name"], "FastAPI")
        self.assertEqual(stack_plan["modules"][1]["primary"]["name"], "Keycloak")
        self.assertIn("# 后台示例 组件拼装包", (output_dir / "README.md").read_text(encoding="utf-8"))
        self.assertIn("FastAPI", (output_dir / "component-manifest.md").read_text(encoding="utf-8"))
        self.assertIn("| Keycloak | auth | Apache-2.0 | 高 | 高 |", (output_dir / "risk-check.md").read_text(encoding="utf-8"))
        integration_plan = (output_dir / "integration-plan.md").read_text(encoding="utf-8")
        self.assertIn("# 集成实施计划", integration_plan)
        self.assertIn("| 1 | 认证 / IAM / Keycloak | 只需要轻量登录。 |", integration_plan)
        self.assertLess(integration_plan.index("Keycloak"), integration_plan.index("FastAPI"))
        architecture_map = (output_dir / "architecture-map.md").read_text(encoding="utf-8")
        self.assertIn("# 组件架构图", architecture_map)
        self.assertIn("前端/客户端 --> 后端 / API / FastAPI", architecture_map)
        self.assertIn("后端 / API / FastAPI --> 认证 / IAM / Keycloak", architecture_map)
        self.assertIn("| 前端/客户端 | 后端 / API / FastAPI |", architecture_map)
        assembly_checklist = (output_dir / "assembly-checklist.md").read_text(encoding="utf-8")
        self.assertIn("# 项目拼装执行清单", assembly_checklist)
        self.assertIn("## 1. 认证 / IAM / Keycloak", assembly_checklist)
        self.assertIn("- [ ] 负责人:", assembly_checklist)
        self.assertIn("- [ ] 先确认许可证和部署方式，再跑通最小样例", assembly_checklist)
        self.assertIn("## 2. 后端 / API / FastAPI", assembly_checklist)
        self.assertLess(assembly_checklist.index("Keycloak"), assembly_checklist.index("FastAPI"))
        env_example = (output_dir / ".env.example").read_text(encoding="utf-8")
        self.assertIn("# 后台示例 环境变量样例", env_example)
        self.assertIn("# 不要在这个文件里填写真实密钥", env_example)
        self.assertIn("BACKEND_FASTAPI_URL=", env_example)
        self.assertIn("BACKEND_FASTAPI_ENABLED=false", env_example)
        self.assertIn("AUTH_KEYCLOAK_URL=", env_example)
        project_readme = (output_dir / "PROJECT-README.md").read_text(encoding="utf-8")
        self.assertIn("# 后台示例", project_readme)
        self.assertIn("## 技术栈总览", project_readme)
        self.assertIn("| 后端 / API | FastAPI | NestJS |", project_readme)
        self.assertIn("## 优先集成顺序", project_readme)
        self.assertIn("1. 认证 / IAM / Keycloak", project_readme)
        self.assertIn("[component-manifest.md](component-manifest.md)", project_readme)
        github_issues = (output_dir / "github-issues.md").read_text(encoding="utf-8")
        self.assertIn("# GitHub Issue 草案", github_issues)
        self.assertIn("## Issue 1: 接入 认证 / IAM / Keycloak", github_issues)
        self.assertIn("标签: `component`, `integration`, `auth`, `risk-high`", github_issues)
        self.assertIn("- [ ] 先确认许可证和部署方式，再跑通最小样例", github_issues)
        self.assertIn("- [ ] 更新 `component-manifest.md`、`risk-check.md` 和 `PROJECT-README.md`", github_issues)
        self.assertLess(github_issues.index("Keycloak"), github_issues.index("FastAPI"))
        github_labels = json.loads((output_dir / "github-labels.json").read_text(encoding="utf-8"))
        label_names = [label["name"] for label in github_labels]
        self.assertEqual(label_names[0], "component")
        self.assertIn("integration", label_names)
        self.assertIn("risk-high", label_names)
        self.assertIn("risk-low", label_names)
        self.assertIn("backend", label_names)
        self.assertIn("auth", label_names)
        auth_label = next(label for label in github_labels if label["name"] == "auth")
        self.assertEqual(auth_label["color"], "1d76db")
        self.assertIn("认证 / IAM", auth_label["description"])


if __name__ == "__main__":
    unittest.main()
