# GitHub Actions Workflows

This project includes GitHub Actions workflows for automated building, testing, and deployment.

## Workflows

### 1. Build and Deploy (`build-and-deploy.yml`)

**Trigger Events:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop`
- Tag pushes matching `v*` pattern (e.g., `v1.0.0`)

**Jobs:**

#### Build and Test Job
- Runs on Ubuntu (latest)
- Tests on Python 3.8, 3.9, 3.10, and 3.11
- Steps:
  1. Checks out code
  2. Sets up Python environment
  3. Installs Poetry and project dependencies
  4. Runs pytest tests
  5. Caches dependencies for faster builds

#### Create Release Job
- Triggers only on version tags (e.g., `v1.0.0`)
- Requires successful build-and-test job
- Steps:
  1. Checks out code
  2. Builds distribution packages using Poetry
  3. Creates a GitHub Release with built artifacts
  4. Optionally publishes to PyPI (requires setup - see below)

### 2. Deploy Workflow (`deploy.yml`)

**Trigger Events:**
- After successful `build-and-deploy` workflow completion

**Purpose:**
- Monitors successful builds on the main branch
- Downloads build artifacts
- Updates deployment status

## Setup Instructions

### 1. Enable GitHub Actions
- Go to your repository settings
- Navigate to **Actions** > **General**
- Ensure **Actions permissions** is set to allow workflows

### 2. Create Tags for Releases
To trigger the release job, create and push a git tag:

```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

### 3. PyPI Deployment (Optional)

To enable automatic publishing to PyPI:

1. Create a PyPI API token:
   - Go to [PyPI.org](https://pypi.org)
   - Navigate to Account Settings > API tokens
   - Create a new token for your project

2. Add secret to GitHub repository:
   - Go to repository **Settings** > **Secrets and variables** > **Actions**
   - Click **New repository secret**
   - Name: `PYPI_API_TOKEN`
   - Value: (paste your PyPI token)

3. Uncomment or verify the PyPI publish step in `build-and-deploy.yml`

## GitHub Secrets Required

| Secret Name | Purpose | Where to Get |
|-------------|---------|-------------|
| `GITHUB_TOKEN` | Create releases and artifacts | Built-in (auto-configured) |
| `PYPI_API_TOKEN` | Publish to PyPI (optional) | [PyPI Account Settings](https://pypi.org/account/settings/) |

## Workflow Status

- View workflow runs: Go to **Actions** tab in your repository
- Check logs for each job by clicking on a workflow run
- Download artifacts from the workflow summary page

## Common Commands

### Run locally
```bash
poetry install
poetry run pytest -v
poetry run python main.py sample_input.txt output.txt
```

### Create a release
```bash
# Update version in pyproject.toml
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

### Build distribution
```bash
poetry build
```

## Customization

To modify the workflows:

1. **Change Python versions**: Edit the `python-version` matrix in `build-and-deploy.yml`
2. **Add more branches**: Update the `branches` list under `on.push` and `on.pull_request`
3. **Add additional test steps**: Insert new steps in the appropriate job
4. **Modify release triggers**: Update the tag pattern or conditions

## Troubleshooting

- **Workflows not running**: Check GitHub Actions are enabled in Settings
- **Build failures**: Review logs in the Actions tab
- **PyPI publish fails**: Verify `PYPI_API_TOKEN` secret is set correctly
- **Poetry install fails**: Ensure `poetry.lock` is committed to the repository

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [PyPI Publishing Guide](https://python-poetry.org/docs/repositories/#publishingto-pypi)
