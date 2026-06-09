# GitHub 发布指南

这个仓库已经是本地 Git 仓库。发布到 GitHub 时，按下面步骤操作。

## 1. 在 GitHub 创建仓库

建议仓库名：

```text
open-source-component-catalog
```

仓库说明可以写：

```text
按模块整理可拼装项目的开源组件目录。
```

更多仓库描述、Topics 和发布后检查项见 [repository-profile.md](repository-profile.md)。

创建仓库时不要勾选自动生成 README、.gitignore 或 License，因为本地仓库已经有这些基础文件。

## 2. 添加远程地址

把下面命令中的地址替换成你自己的 GitHub 仓库地址：

```powershell
git remote add origin https://github.com/<your-user>/open-source-component-catalog.git
git remote -v
```

如果你使用 SSH：

```powershell
git remote add origin git@github.com:<your-user>/open-source-component-catalog.git
git remote -v
```

## 3. 运行发布前检查

推送前先运行整合检查：

```powershell
python tools/pre_publish_check.py
```

这个命令会运行组件目录校验、内置项目预设的成熟开源覆盖审计、完整单元测试，并提示是否已经配置 GitHub 远端。没有远端时不会让本地校验失败，但发布前仍需要添加 `origin`。

## 4. 推送主分支

当前本地分支是 `master`。可以直接推送：

```powershell
git push -u origin master
```

如果你希望 GitHub 主分支叫 `main`，先重命名再推送：

```powershell
git branch -M main
git push -u origin main
```

## 5. 替换 CODEOWNERS

发布后编辑 [.github/CODEOWNERS](../.github/CODEOWNERS)，把占位负责人替换成真实 GitHub 用户或团队。

示例：

```text
* @your-github-user
```

## 6. 检查 Actions

推送后打开 GitHub 仓库的 Actions 页面，确认“校验组件目录”工作流通过。

这个工作流会执行：

```powershell
python tools/validate_catalog.py --write-index
python tools/audit_mature_coverage.py --preset saas-starter --fail-on-missing
python tools/audit_mature_coverage.py --preset ai-rag-app --fail-on-missing
python tools/audit_mature_coverage.py --preset internal-admin --fail-on-missing
python -m unittest tests.test_validate_catalog -v
python -m unittest tests.test_search_catalog -v
python -m unittest tests.test_audit_mature_coverage -v
python -m unittest tests.test_stack_presets -v
python -m unittest tests.test_assemble_stack -v
python -m unittest tests.test_summarize_catalog -v
python -m unittest tests.test_check_stack -v
python -m unittest tests.test_generate_worksheet -v
python -m unittest tests.test_generate_project_package -v
python -m unittest tests.test_pre_publish_check -v
```

如果 `catalog/index.json` 没有同步更新，或搜索、成熟开源覆盖审计、预设、拼装、概览、风险检查、工作表生成和发布前检查脚本出现回归，CI 会失败，提醒你修复后再推送。
