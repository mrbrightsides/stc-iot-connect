# Contributing to STC IoT Connect

Thank you for your interest in contributing to STC IoT Connect! This document provides guidelines and instructions for contributing to this project.

## 🌟 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:
- Node.js 18+ installed
- Git configured with your GitHub account
- Basic understanding of TypeScript, React, and Next.js
- Familiarity with blockchain concepts (for blockchain-related contributions)

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/stc-iot-connect.git
   cd stc-iot-connect
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your configuration
   ```

4. **Run development server**
   ```bash
   npm run dev
   ```

5. **Open http://localhost:3000**

## 📝 How to Contribute

### Reporting Bugs

When reporting bugs, please include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, Node version, browser)

**Template:**
```markdown
## Bug Description
Brief description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., macOS 14.0]
- Node: [e.g., 18.17.0]
- Browser: [e.g., Chrome 120]
```

### Suggesting Features

For feature requests, please include:

- **Clear use case** - Why is this feature needed?
- **Proposed solution** - How should it work?
- **Alternatives considered** - What other approaches did you think about?
- **Additional context** - Screenshots, mockups, examples

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Follow the coding standards (see below)
   - Add tests if applicable
   - Update documentation

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**
   - Provide a clear title and description
   - Reference any related issues
   - Include screenshots for UI changes
   - Wait for review

### Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
feat(api): add device health monitoring endpoint
fix(ui): correct menu alignment in mobile view
docs(readme): update installation instructions
refactor(auth): simplify JWT validation logic
```

## 🎨 Coding Standards

### TypeScript

- Use **explicit types** for all variables, parameters, and return values
- Avoid `any` type - use proper typing
- Use interfaces for object types
- Export types that might be reused

```typescript
// ✅ Good
interface DeviceConfig {
  id: string;
  name: string;
  enabled: boolean;
}

function updateDevice(config: DeviceConfig): Promise<void> {
  // implementation
}

// ❌ Bad
function updateDevice(config: any) {
  // implementation
}
```

### React Components

- Use **functional components** with hooks
- Extract reusable logic into custom hooks
- Keep components small and focused
- Use proper prop typing

```typescript
// ✅ Good
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

export function CustomButton({ label, onClick, disabled = false }: ButtonProps) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

### File Organization

```
src/
├── app/                    # Next.js app router
│   ├── api/               # API routes
│   └── page.tsx           # Main page
├── components/            # Reusable components
│   └── ui/               # UI components (shadcn)
├── lib/                   # Utility functions
└── types/                 # TypeScript type definitions
```

### API Development

- Use RESTful conventions
- Return consistent response formats
- Include proper error handling
- Add rate limiting for production endpoints

```typescript
// Consistent API response format
{
  success: true,
  data: { ... },
  message: "Operation successful"
}

// Error format
{
  success: false,
  error: "Error message",
  code: "ERROR_CODE"
}
```

### Styling

- Use **Tailwind CSS** for styling
- Follow mobile-first approach
- Ensure responsive design
- Maintain dark mode compatibility (where applicable)

## 🧪 Testing

### Running Tests

```bash
npm run test          # Run all tests
npm run test:watch    # Run tests in watch mode
npm run test:coverage # Generate coverage report
```

### Writing Tests

- Write tests for new features
- Maintain test coverage above 70%
- Test edge cases and error scenarios
- Use descriptive test names

```typescript
describe('DeviceManager', () => {
  it('should add a new device successfully', async () => {
    // Test implementation
  });

  it('should handle duplicate device IDs', async () => {
    // Test implementation
  });
});
```

## 📚 Documentation

When contributing, please update:

- **README.md** - For major features or setup changes
- **API.md** - For new API endpoints
- **Code comments** - For complex logic
- **Type definitions** - For new interfaces/types

## 🔍 Code Review Process

### What We Look For

- ✅ Code quality and readability
- ✅ Proper TypeScript typing
- ✅ Test coverage
- ✅ Documentation updates
- ✅ No breaking changes (without discussion)
- ✅ Performance considerations

### Review Timeline

- **Initial response**: Within 2-3 days
- **Full review**: Within 1 week
- **Merge decision**: Based on complexity and impact

## 🏗️ Project Structure

### Key Directories

- **`/src/app`** - Next.js pages and API routes
- **`/src/components`** - React components
- **`/src/lib`** - Utility functions and helpers
- **`/public`** - Static assets

### Important Files

- **`src/app/page.tsx`** - Main application UI
- **`src/app/api/*`** - API endpoint implementations
- **`package.json`** - Dependencies and scripts
- **`tsconfig.json`** - TypeScript configuration

## 🤝 Community

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and ideas
- **Documentation**: Check README.md and other docs first

### Recognition

Contributors will be:
- Added to the contributors list
- Mentioned in release notes
- Credited in the README

## 📋 Checklist Before Submitting PR

- [ ] Code follows the style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added and passing
- [ ] Commit messages follow convention
- [ ] Branch is up to date with main

## 🎯 Areas to Contribute

### Good First Issues

- Documentation improvements
- UI/UX enhancements
- Bug fixes
- Test coverage improvements

### Advanced Contributions

- New device integrations
- Blockchain optimizations
- Performance improvements
- Security enhancements
- Real-time features

## 📞 Contact

For questions about contributing:
- Open a GitHub Discussion
- Tag maintainers in issues
- Check existing issues and PRs

---

Thank you for contributing to STC IoT Connect! Your efforts help make this project better for everyone. 🚀
