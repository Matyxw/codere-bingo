import { useState } from "react";
import { api } from "../lib/api";

export default function NuevaCompra() {
  const [form, setForm] = useState({ operador_id: "", puesto_id: "", cantidad_cartones: 1, importe_total: 0, cliente_nombre: "" });
  const [res, setRes] = useState<any>(null);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const r = await api.post("/compras", form);
    setRes(r.data);
  };

  return (
    <section className="rounded-2xl border border-border-subtle bg-bg-card p-4 space-y-3">
      <h2 className="text-base font-semibold">Nueva compra</h2>
      <form onSubmit={submit} className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <input className="rounded-xl border border-border-subtle bg-black/40 px-3 py-2" placeholder="operador_id" value={form.operador_id} onChange={e => setForm({ ...form, operador_id: e.target.value })} />
        <input className="rounded-xl border border-border-subtle bg-black/40 px-3 py-2" placeholder="puesto_id" value={form.puesto_id} onChange={e => setForm({ ...form, puesto_id: e.target.value })} />
        <input className="rounded-xl border border-border-subtle bg-black/40 px-3 py-2" type="number" min={1} max={6} value={form.cantidad_cartones} onChange={e => setForm({ ...form, cantidad_cartones: Number(e.target.value) })} />
        <input className="rounded-xl border border-border-subtle bg-black/40 px-3 py-2" type="number" min={0} step="0.01" value={form.importe_total} onChange={e => setForm({ ...form, importe_total: Number(e.target.value) })} />
        <input className="rounded-xl border border-border-subtle bg-black/40 px-3 py-2 md:col-span-2" placeholder="cliente_nombre" value={form.cliente_nombre} onChange={e => setForm({ ...form, cliente_nombre: e.target.value })} />
        <button className="rounded-full border border-border-subtle bg-ok/10 px-4 py-2 text-ok" type="submit">Generar compra</button>
      </form>
      {res && (
        <div className="rounded-2xl border border-border-subtle bg-black/30 p-4 space-y-2">
          <div className="flex flex-wrap gap-2 text-sm">
            <span className="rounded-full border border-border-subtle bg-white/5 px-3 py-1">ID: {res.id}</span>
            <span className="rounded-full border border-border-subtle bg-white/5 px-3 py-1">Cartones: {res.cantidad_cartones}</span>
            <span className="rounded-full border border-border-subtle bg-white/5 px-3 py-1">Importe: ${res.importe_total}</span>
          </div>
          <pre className="text-xs opacity-80">{JSON.stringify(res, null, 2)}</pre>
        </div>
      )}
    </section>
  );
}
