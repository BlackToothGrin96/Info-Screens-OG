import { dev } from '$app/environment';
import {error} from "@sveltejs/kit";
import type {PageServerLoad} from './$types';

// we don't need any JS on this page, though we'll load
// it in dev so that we get hot module replacement
export const csr = dev;

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = false;

export const load: PageServerLoad = async ({ params }) => {
    // const channelInfo = await fetch(
    //     'http://192.168.1.155:8000/info/channel/' + params.channel_code);
    //
    // const res = await channelInfo.json();
    //
    // let total = 0;
    //
    // res.statuses.forEach((item: any) => {
    //     total += item.count;
    // });

    const result = {
        // "info": res,
        // "total": total,
        "channel_code": params.channel_code,
    }

    console.log("result: ", result);

    return result;
};