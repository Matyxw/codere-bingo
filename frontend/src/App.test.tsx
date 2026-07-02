import { test, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "../App";

test("renderiza el componente App", () => {
  render(<App />);
  expect(document.body).toBeDefined();
});
