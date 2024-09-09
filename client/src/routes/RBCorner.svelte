<script>
	import logo from '$lib/images/logo@2x.png';
</script>

<div class="rb-corner">
    <div class="columns is-multiline">
        <div class="column is-full logo">
            <img src={logo} alt="RexBrown Innovations" />
        </div>
<!--        <div class="column is-full time-container">-->
<!--            <p class="time-text">{padToTwoDigits(hours)}:{padToTwoDigits(minutes)}:{padToTwoDigits(seconds)} - {date}</p>-->
<!--        </div>-->
    </div>
<!--    <p>{hours}:{minutes}:{seconds}</p>-->
</div>


<style>
    .rb-corner {
        position: fixed;
        bottom: 0;
        left: 0;
        background: var(--rb-primary);
        border-top-right-radius: 25px;
        width: 24%;
        height: 15%;
        display: flex;
        /*padding-bottom: 5px;*/
        /*padding-right: 5px;*/
    }

    .logo > img {
        display: block;
        /*margin-left: auto;*/
        /*margin-right: auto;*/
        height: auto;
        width: 90%;
        /*flex: 1;*/
        /*padding: 10%;*/
        /*padding-top: 25px;*/
        /*padding-bottom: 25px;*/
        /*padding-right: 10px;*/
        /*padding-left: 25px;*/
    }

    .logo {
        height: 100%;
        width: 100%;
        /*margin-top: 20px;*/
        /*margin-bottom: 20px;*/
        /*padding-top: 1rem;*/
    }

    .columns {
        /*display: flex;*/
        /*align-items: center;*/
        /*justify-content: center;*/
        width: 100%;
        height: 100%;
    }

    .column {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /*.time-container {*/
    /*    height: 30%;*/
    /*}*/

	/*.time-text {*/
	/*	color: white;*/
	/*	font-weight: bold;*/
	/*	font-size: 2rem;*/
	/*	text-align: center;*/
	/*	margin: 0;*/
	/*}*/
</style>