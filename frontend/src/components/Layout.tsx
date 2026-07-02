import { Outlet } from "react-router-dom";

export default function Layout({ children }: { children?: React.ReactNode }) {
  const content = children ?? <Outlet />;
  return (
    <div className="p-6 max-w-6xl mx-auto space-y-4">
      <header className="flex items-center justify-between gap-3 rounded-2xl border border-border-subtle bg-bg-card px-5 py-4">
        <div className="text-lg font-semibold">Codere Bingo</div>
        <div className="flex gap-2 text-sm text-tx-1/80">
          <span className="rounded-full border border-border-subtle bg-white/5 px-3 py-1">Sala: bingo-01</span>
          <span className="rounded-full border border-border-subtle bg-white/5 px-3 py-1">Puesto: ventanilla-3</span>
        </div>
      </header>
      {content}
    </div>
  );
}
