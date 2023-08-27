import { defineComponent } from "vue";
import { Excalidraw } from "@excalidraw/excalidraw";




export default defineComponent({
	components: {
		Excalidraw,
	},
	render() {
		return <Excalidraw />;
	},
});
