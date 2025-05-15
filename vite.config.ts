import { defineConfig, type UserConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";

export default defineConfig(({ mode }) => {
	const config: UserConfig = {
		// root directory
		root: path.resolve(__dirname, "frontend"),

		plugins: [react()],
	};

	return config;
});
