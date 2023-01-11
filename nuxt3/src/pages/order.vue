<template>
  <NuxtLayout>
	<div class="loading" v-if="isLoading">
	  Loading...
	</div>
	<LastOrder :orderData="order" v-else-if="order"/>
	<SandWichForm v-else @submitForm="submitOrder"/>
  </NuxtLayout>
</template>

<script>
import { formatDateString } from "~/utils"

export default {
	setup() {
    definePageMeta({
      middleware: "require-auth",
    }) // options API doesn't seem to work

		const appConfig = useAppConfig();
		return { appConfig };
	},
	data() {
		return {
			isLoading: false,
			order: null
		};
	},
	created() {
		this.fetchOrder();
	},
	methods: {
		fetchOrder() {
			this.isLoading = true;

			// ask API if there's an order already saved
			fetch(
				this.appConfig.API_URL + "/orders/?order_date=" + formatDateString(new Date()),
				{
					headers: {
						"Content-Type": "application/json",
						"Authorization": "Token " + localStorage.getItem("API_token")
					}
				}
			)
				.then(res => res.json())
				.then(json => {
					this.order = (json.length == 0) ? null : json[0];
					this.isLoading = false;
				}); // no error handling :(
		},
		submitOrder(data) {
			this.isLoading = true;

			// submit an order to the API
			fetch(this.appConfig.API_URL + "/orders/", {
				method: "POST",
				headers: {
          "Content-Type": "application/json",
          "Authorization": "Token " + localStorage.getItem("API_token")
        },
				body: JSON.stringify(data)
			})
				.then(res => res.json())
				.then(json => {
					this.order = json;
					this.isLoading = false;
				}); // no error handling :(
		}
	}
}
</script>
