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
    try {
        const channelInfo = await fetch(
            'http://192.168.1.30:8000/info/channel/KITANDKIN');

        if (!channelInfo.ok) {
            throw new Error('Failed to fetch data');
        }

        const res = await channelInfo.json();

        let total = 0;

        res.statuses.forEach((item: any) => {
            total += item.count;
        });

        const result = {
            "info": res,
            "total": total,
            "channel_code": params.channel_code,
        }

        console.log("result: ", result);

        return result;
    } catch (error) {
        console.error('Fetch failed:', error);
        return { data: null };  // Return fallback data or null to avoid breaking the build
    }
};