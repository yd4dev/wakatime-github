const axios = require('axios');
require('dotenv').config();

const GITHUB_API = 'https://api.github.com/user'
const WAKATIME_API = 'https://wakatime.com/api/v1/users/current/summaries'

async function getWakaTime() {
	let res = null;
	try {
		res = await axios({
			method: "GET",
			url: WAKATIME_API,
			params: {
				api_key: process.env.WAKATIME_API_KEY,
				scope: "read_logged_time",
				start: new Date(Date.now()),
				end: new Date(Date.now()),
			},
		});
		return res.data.data[0].grand_total.text;
	} catch (err) {
		console.error(err);
	}
}

async function updateBio() {

	const total = await getWakaTime();
	const today = new Date().toLocaleDateString();

	const message = `Today (${today}) Coded: ${total}`;

	try {
		await axios({
			method: "PATCH",
			url: GITHUB_API,
			headers: {
				Accept: "application/vnd.github.v3+json",
				Authorization: `token ${process.env.GITHUB_API_KEY}`,
			},
			data: {
				bio: message,
			},
		});
	} catch (err) {
		console.error(err);
	}
}
updateBio();
/* Update bio every 15 minutes */
setTimeout(updateBio, 900000);