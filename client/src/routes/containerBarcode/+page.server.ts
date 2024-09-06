import { dev } from '$app/environment';
import {error} from "@sveltejs/kit";
// import type {PageServerLoad} from './$types';

// we don't need any JS on this page, though we'll load
// it in dev so that we get hot module replacement
export const csr = dev;

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;

// export const load: PageServerLoad = async ({ params }) => {
//     const container = await fetch(
//         'http://192.168.1.194:8000/staging/fetch_container?container_barcode=' + params.containerBarcode);
//     const res = await container.json();
//     console.log("res: ", res);
//
//     return res;
// };