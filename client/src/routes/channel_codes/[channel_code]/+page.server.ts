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
    const channel_name = await fetch(
        'http://192.168.1.30:8000/info/name/' + params.channel_code);
    const channel_codes = await fetch(
        'http://192.168.1.30:8000/info/channel_codes/' + params.channel_code);
    const modules = await fetch(
        'http://192.168.1.30:8000/info/modules/' + params.channel_code);

    // let total = 0;
    //
    // res.statuses.forEach((item: any) => {
    //     total += item.count;
    // });

    const result = {
        "channel_code": params.channel_code,
        "channel_name": await channel_name.json(),
        "channel_codes": await channel_codes.json(),
        "modules": await modules.json(),
    }

    console.log("result: ", result);

    return result;
};
