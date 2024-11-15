import { dev } from '$app/environment';
import {error} from "@sveltejs/kit";
import type {PageServerLoad} from './$types';

const apiUrl = import.meta.env.VITE_API_URL;

// we don't need any JS on this page, though we'll load
// it in dev so that we get hot module replacement
export const csr = dev;

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;

export const load: PageServerLoad = async ({ params }) => {
    const channelInfo = await fetch(
        'http://192.168.1.30:8000/info/total_channels');

    const res = await channelInfo.json();

    const result = {
        "channels": res,
    }

    console.log("result: ", result);

    return result;
};