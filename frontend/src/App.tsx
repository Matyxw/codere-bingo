import { Suspense, lazy } from "react";
import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";

const NuevaCompra = lazy(() => import("./pages/nueva-compra"));
const ValidarTicket = lazy(() => import("./pages/validar-ticket"));

export default function App() {
  return (
    <Suspense fallback={<div className="p-6">Cargando...</div>}>
      <Layout>
        <Routes>
          <Route path="/" element={<NuevaCompra />} />
          <Route path="/validar" element={<ValidarTicket />} />
        </Routes>
      </Layout>
    </Suspense>
  );
}
