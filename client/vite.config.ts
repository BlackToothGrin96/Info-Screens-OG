import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import path from 'path';

// const apiUrl = import.meta.env.VITE_API_URL;

export default defineConfig({
	// define: {
	// 	'process.env.API_URL': JSON.stringify(process.env.VITE_API_URL)
	// },
	plugins: [sveltekit()],
	// resolve: {
	// 	alias: {
	// 	  "@": path.resolve(__dirname, "./src"),
	// 	},
	// },
	// Aliases: https://dev.to/danawoodman/how-to-add-module-import-aliases-in-sveltekit-2ck
	resolve: {
		alias: {
			"$": path.resolve(__dirname, "/src"),
		}
	},
	server: {
		proxy: {
			// A local Docker Compose environment has two containers and networking is performed by referencing the
			//     container names, which are found in the `docker-compose.yml` and `docker-compose.dev.yml` files.
			"/api": 'http://192.168.1.30:8000', // Used in Docker dev environments.
			// "/api": "http://your-k8s-url-goes-here:8000", // Used for deployments to Kubernetes.
					// "/api": "http://localhost:8000" // Used in non-Docker dev environments.
		}
	}
});
