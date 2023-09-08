import React from "react";
import { Excalidraw, MainMenu, Footer } from "@excalidraw/excalidraw";

const UIOptions = {
	canvasActions: {
		changeViewBackgroundColor: false,
		clearCanvas: false,
		loadScene: false,
	},
};

const button = () => {
	return (
		<button
			style={{
				background: "#70b1ec",
				border: "none",
				color: "#fff",
				width: "max-content",
				fontWeight: "bold",
				width: "100px",
				borderRadius: "5px",
			}}
		>
			AI
		</button>
	);
};

class ExcalidrawIntegration extends React.Component {
	render() {
		return (
			<div style={{ width: "100%", height: "100%" }}>
				<Excalidraw UIOptions={UIOptions} renderTopRightUI={button}>
					<MainMenu>
						<MainMenu.Item>
							<a href="/">Home</a>
						</MainMenu.Item>
					</MainMenu>
				</Excalidraw>
			</div>
		);
	}
}

export default ExcalidrawIntegration;
