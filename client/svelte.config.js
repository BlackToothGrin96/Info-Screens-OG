// __dirname is not available in ES modules: https://nodejs.org/api/esm.html#esm_no_filename_or_dirname
// This issue has a fix: https://github.com/nodejs/help/issues/2907
import path from "path";
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
import adapter from "@sveltejs/adapter-static";
import preprocess from "svelte-preprocess";

/** @type {import("@sveltejs/kit").Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: preprocess({
    typescript: {
      tsconfigFile: path.resolve(__dirname, './tsconfig.json'), // Add this line
    },
  }),

	kit: {
    // Configure for SPA mode. Specify your HTML file as the fallback file.
    // TROUBLESHOOTING NOTE:
    // If you get this error when you run `npm run dev`: `config.kit.adapter should be an object with an "adapt" method`
    // ...then install "@sveltejs/adapter-static" with the following command:
    // npm install --save-dev @sveltejs/adapter-static@next
    // Notice the `@next` that is included at the end of the package name.
		adapter: adapter({
      fallback: "index.html"
    }),

    alias: {
        // this will match a file
        'app.html': path.resolve(__dirname, './src/app.html'),
    },

    prerender: {
      handleHttpError: ({ status, path, referrer, referenceType }) => {
        if (status === 500) {
          console.warn(`Prerendering failed for ${path} with status ${status}`);
          // Ignore the error or handle accordingly
          return;
        }

        // Handle other errors or log them
      }
    }

    // If you want to rename the `index.html` file to something else, then you need to provide the file path along with
		// the name of the HTML file in this `files.template` setting. The default setting is "src/index.html".
    // files: {
    //   template: "index.html",
    // },

		// hydrate the <div id="svelte"> element in src/index.html
		// target: "#svelte",

    // vite: () => ({
	// 		// For Development: Set the proxy server to the port that the Python code will run on.
  	// 	// Fix the server.proxy errors:
	// 		// https://stackoverflow.com/questions/61823628/getting-vue-devserver-proxy-to-work-with-different-local-ports-in-docker.
	// 		server: {
	// 			proxy: {
    //       // A local Docker Compose environment has two containers and networking is performed by referencing the
	// 	  //     container names, which are found in the `docker-compose.yml` and `docker-compose.dev.yml` files.
	// 				"/api": "http://dev-server:8000", // Used in Docker dev environments.
    //       // "/api": "http://your-k8s-url-goes-here:8000", // Used for deployments to Kubernetes.
	// 				// "/api": "http://localhost:8000" // Used in non-Docker dev environments.
	// 			}
	// 		},
    //
	// 		// Aliases: https://dev.to/danawoodman/how-to-add-module-import-aliases-in-sveltekit-2ck
	// 		resolve: {
	// 			alias: {
	// 				"$": path.resolve(__dirname, "/src"),
	// 			}
	// 		},
	// 	}),
	}
};

export default config;
