<template>
  <div class="loading" v-if="isLoading">
    Loading...
  </div>
  <LastOrder :orderData="order" v-else-if="order"/>
  <SandWichForm v-else @submitForm="submitOrder"/>
</template>

<script>
export default {
    setup() {
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
            fetch(this.appConfig.API_URL + "/orders?today")
                .then(res => res.json())
                .then(json => {
                this.order = (json.length == 0) ? null : json;
                this.isLoading = false;
            }); // no error handling :(
        },
        submitOrder(data) {
            this.isLoading = true;
            // submit an order to the API
            fetch(this.appConfig.API_URL + "/orders", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
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
