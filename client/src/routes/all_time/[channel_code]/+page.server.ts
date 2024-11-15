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
    const openOrders = await fetch(
        'http://192.168.1.30:8000/info/open/' + params.channel_code);
    const otherNumbers = await fetch(
        'http://192.168.1.30:8000/info/others/' + params.channel_code);
    const oldestOrder = await fetch(
        'http://192.168.1.30:8000/info/oldest/' + params.channel_code);
    const carriers = await fetch(
        'http://192.168.1.30:8000/info/active_couriers/' + params.channel_code);

    const open = await openOrders.json();
    const other = await otherNumbers.json();
    const oldest = await oldestOrder.json();
    const couriers = await carriers.json();

    if (open === 0) {
        couriers.sort((a: any, b: any) => {
            return b.total_count - a.total_count;
        });
    }

    // let total = 0;
    //
    // res.statuses.forEach((item: any) => {
    //     total += item.count;
    // });

    const result = {
        "channel_name": await channel_name.json(),
        "open": open,
        "other": other,
        "oldest": oldest,
        "couriers": couriers,
        "channel_code": params.channel_code,
    }

    console.log("result: ", result);

    return result;
};