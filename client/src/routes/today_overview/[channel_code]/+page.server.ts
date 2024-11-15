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
    const open = await fetch(
        'http://192.168.1.30:8000/info/open/' + params.channel_code);
    const new_today = await fetch(
        'http://192.168.1.30:8000/info/new_today/' + params.channel_code);
    const other_numbers = await fetch(
        'http://192.168.1.30:8000/info/others/' + params.channel_code);
    var oldest = await fetch(
        'http://192.168.1.30:8000/info/oldest/' + params.channel_code);
    const cancelled = await fetch(
        'http://192.168.1.30:8000/info/cancelled/' + params.channel_code);
    const priority = await fetch(
        'http://192.168.1.30:8000/info/priority/' + params.channel_code);

    // let total = 0;
    //
    // res.statuses.forEach((item: any) => {
    //     total += item.count;
    // });

    const result = {
        "channel_code": params.channel_code,
        "channel_name": await channel_name.json(),
        "open": await open.json(),
        "new": await new_today.json(),
        "other": await other_numbers.json(),
        "oldest": await oldest.json(),
        "cancelled": await cancelled.json(),
        "priority": await priority.json(),
    }

    console.log("result: ", result);

    return result;
};