import { useState } from "react";
import { api } from "../lib/api";

export default function ValidarTicket() {
  const [qr, setQr] = useState("");
  const [res, setRes] = useState<any>(null);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const r = await api.post("/tickets/validar", { qr_payload: qr });
    setRes(r.data);
  };

  return (
    <section className="rounded-2xl border border-border-subtle bg-bg-card p-4 space-y-3">
      <h2 className="text-base font-semibold">Validar ticket</h2>
      <form onSubmit={submit} className="grid grid-cols-1 md:grid-cols-2 gap-3">
        <input className="rounded-xl border border-border-subtle bg-black/40 px-3 py-2" placeholder="qr_payload" value={qr} onChange={e => setQr(e.target.value)} />
        <button className="rounded-full border border-border-subtle bg-ok/10 px-4 py-2 text-ok" type="submit">Validar</button>
      </form>
      {res && (
        <div className="rounded-2xl border border-border-subtle bg-black/30 p-4 space-y-2">
          <h3 className="text-sm font-semibold">Resultado validación</h3>
          <pre className="text-xs opacity-80">{JSON.stringify(res, null, 2)}</pre>
        </div>
      )}
    </section>
  );
}
