# Contributing to Phyllux

Good faith contributions only. Follow ethical tiers. Empirical contributions welcome; cite PPA for alignment.

## Ethical IP Tiers

1. **Free Tier** — Research, education, open-source contributions
2. **Commercial Tier** — Fair royalties for profit use
3. **Pioneer Tier** — Low/no-fee for high-impact players (sustainability, space, longevity orgs)
4. **Community Defense** — No misuse; revocation for bad faith; shared prosperity, no patent trolling

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Getting Started

1. **Fork the repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/biomimetic-inventions-public.git
   cd biomimetic-inventions-public
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a branch for your changes:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Contribution Guidelines

### Code Standards

- **Good Faith**: All contributions must be made in good faith with the goal of advancing the technology
- **Code Style**: Follow existing code style and naming conventions
  - Python: Use snake_case for functions/variables, PascalCase for classes
  - Include docstrings for all functions and classes
  - Follow PEP 8 style guide
- **Documentation**: Update relevant documentation when adding features
- **Testing**: Include tests where applicable (simulation-based validation)
- **Comments**: Add comments for complex logic, but prefer self-documenting code

### Code Header Template

All Python files should include a header:

```python
"""
[filename].py - [Brief description]

Part of Phyllux Technologies - Multi-Domain Phyllotactic Systems
Inventor: David Edward Sproule (@Phibronotchi)
License: MIT (code) / CC BY-SA 4.0 (documentation)
Repository: https://github.com/phibronotchi-beep/biomimetic-inventions-public

[Longer description if needed]
"""
```

### PPA Alignment

Empirical contributions should cite the PPA: "Phyllotactic Multi-Domain System for Neural Interfaces, Wireless Communications, and Cryptographic Security" (prepared for filing, to be filed late January 2026).

### Commit Messages

Use clear, descriptive commit messages:

```
feat: Add new visualization script for PNM electrode arrays
fix: Correct golden angle calculation in phyllotaxis_utils.py
docs: Update README with installation instructions
refactor: Simplify array factor calculation
```

### Pull Request Process

1. **Update your branch** with the latest changes from main:
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. **Test your changes:**
   ```bash
   # Run any relevant example scripts
   python your-script.py
   
   # Check for syntax errors
   python -m py_compile your-script.py
   ```

3. **Push to your fork:**
   ```bash
   git push origin your-branch
   ```

4. **Create a Pull Request** on GitHub with:
   - Clear description of changes
   - Reference to related issues (if any)
   - Screenshots or examples (if applicable)

## Testing

### Running Example Scripts

Test that example scripts still work after your changes:

```bash
# Test PNM examples
python PNM-public/examples/021-phyllux-pnm-3d-spiral-view.py

# Test GAFAA examples
python golden-angle-antenna-GAFAA-public/examples/001-phyllux-gafaa-3d-spiral-view.py

# Test Phyllux Vault examples
python PhiKey-public/examples/011-phyllux-phikey-3d-spiral-view.py
```

### Image Regeneration

If you modify image generation code, verify images regenerate correctly:

```bash
python regenerate_all_images.py
```

## Common Errors and Solutions

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'numpy'`

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Path Detection Issues

**Error:** Scripts can't find repository root

**Solution:** Ensure scripts use portable path detection (check for `README.md` and `LICENSE` files)

### Image Generation Failures

**Error:** Images not generating or have artifacts

**Solution:** 
- Ensure `matplotlib.use('Agg')` is set for headless operation
- Check that `plt.show()` is replaced with `plt.close()`
- Verify white backgrounds with `facecolor='white'`

## PPA Disclaimer

Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).

## Security

If you discover a security vulnerability, please see [SECURITY.md](SECURITY.md) for reporting instructions.

**Do NOT** open a public issue for security vulnerabilities.

## Contact

For questions about contributions or licensing, contact: phibronotchi@gmail.com

## Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.
