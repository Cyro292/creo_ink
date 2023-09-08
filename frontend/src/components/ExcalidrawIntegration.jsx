import React from "react";
import { Excalidraw } from "@excalidraw/excalidraw";

function ExcalidrawIntegration() {
	return (
		<div>
			<h1 style={{ textAlign: "center" }}>Excalidraw Example</h1>
			<div style={{ height: "500px" }}>
				<Excalidraw />
			</div>
		</div>
	);
}

export default ExcalidrawIntegration;
