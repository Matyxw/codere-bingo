import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import App from "../src/App";

describe("App", () => {
  it("muestra el título principal", () => {
    render(<App />);
    expect(screen.getByText("Codere Bingo")).toBeDefined();
  });
});
