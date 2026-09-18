# Project Context

## Stack

- Language: TypeScript
- Framework: React 19
- Build: Vite
- Test: Vitest

## Commands

```bash
npm run dev      # Start dev server
npm run build    # Production build
npm run test     # Run tests
npm run lint     # ESLint check
```

## Architecture

```
src/
├── pages/       # Route components
├── components/  # Shared UI
├── hooks/       # Custom hooks
├── services/    # API calls
└── types/       # TypeScript types
```

## Conventions

- Components: PascalCase (`UserCard.tsx`)
- Hooks: camelCase with `use` prefix (`useAuth.ts`)
- Services: camelCase (`userService.ts`)
- Tests: co-located (`UserCard.test.tsx`)

## Do not

- Add dependencies without discussing
- Modify `tsconfig.json` strictness
- Skip TypeScript types
