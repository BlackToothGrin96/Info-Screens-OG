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
    var orders = await fetch(
        'http://192.168.1.30:8000/go/orders_by_courier_group');
    var pallets = await fetch(
        'http://192.168.1.30:8000/go/pallets_by_courier_group');
    var pallet_scans = await fetch(
        'http://192.168.1.30:8000/go/pallets_loaded_by_courier_group');
    var trucks = await fetch(
        'http://192.168.1.30:8000/go/trucks_by_courier_group');

    const orders_res = await orders.json();
    const pallets_res = await pallets.json();
    const pallet_scans_res = await pallet_scans.json();
    const trucks_res = await trucks.json();

    // Create a map for faster lookup of names in list1
    const pallet_scansMap = new Map(pallet_scans_res.map(item => [item.name, item]));

    // Iterate over list2 and fill in missing items in list1
    const padded_scans = orders_res.map(item => {
      // Check if the name exists in list1
      if (pallet_scansMap.has(item.name)) {
        // If exists, use the count from list1
        return pallet_scansMap.get(item.name)!;
      } else {
        // If doesn't exist, return the name with count 0
        return { count: 0, name: item.name };
      }
    });

    // Create a map for faster lookup of names in list1
    const trucks_resMap = new Map(trucks_res.map(item => [item.name, item]));

    // Iterate over list2 and fill in missing items in list1
    const padded_trucks = orders_res.map(item => {
      // Check if the name exists in list1
      if (trucks_resMap.has(item.name)) {
        // If exists, use the count from list1
        return trucks_resMap.get(item.name)!;
      } else {
        // If doesn't exist, return the name with count 0
        return { count: 0, name: item.name };
      }
    });

    // let total = 0;
    //
    // res.statuses.forEach((item: any) => {
    //     total += item.count;
    // });

    const result = {
        "orders": orders_res,
        "pallets": pallets_res,
        "pallet_scans": padded_scans,
        "trucks": padded_trucks,
    }

    console.log("result: ", result);

    return result;
};
