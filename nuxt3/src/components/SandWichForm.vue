<template>
    <form @submit.prevent="submitForm">
      <div class="inputSet">
        <label for="email" class="green">Email</label>
        <input type="email" name="email" id="email" class="green" required>
      </div>

      <fieldset class="inputSet">
        <legend class="green">Select your sandwich type</legend>
        <div v-for="sandwich in sandwiches">
          <input
            type="radio"
            name="sandwich"
            :id="sandwich.id"
            :value="sandwich.id"
            required
          >
          <label :for="sandwich.id">{{ sandwich.name }}</label>
        </div>
      </fieldset>

      <fieldset class="inputSet">
        <legend class="green">Select your bread type</legend>
        <div>
          <input type="radio" name="breadType" id="brown" value="brown" required>
          <label for="brown">Brown</label>
        </div>
  
        <div>
          <input type="radio" name="breadType" id="white" value="white">
          <label for="white">White</label>
        </div>
      </fieldset>

      <div class="inputSet buttonContainer">
        <button type="submit">Get that bread!</button>
      </div>
    </form>
</template>

<script>
import sandwiches from "../sandwiches"

export default {
  created() {
    this.sandwiches = sandwiches;
  },
  methods: {
    // possibly use v-model instead of collecting the data manually
    submitForm(e) {
      const data = {
        email: e.target.elements.email.value,
        sandwich: e.target.elements.sandwich.value,
        breadType: e.target.elements.breadType.value,
      }

      this.$emit('submitForm', data)
    }
  }
}
</script>

<style scoped>
.inputSet {
  margin: 2rem;
}

fieldset {
  border-width: 2px;
  border-style: solid;
  border-color: var(--color-border);
  border-radius: 2%;
}

label {
  padding: 0.3rem;
}

input[type="email"] {
  color: black;
}

.buttonContainer {
  display: flex;
  justify-content: center;
}

button[type="submit"] {
  border: none;
  padding: 10px;
  background-color: rgb(182, 203, 81);
  box-shadow: 0 0 0px 0px rgba(183, 203, 81, 0.3);
  transition: box-shadow 0.1s ease-in-out;
}

button[type="submit"]:hover {
  border: none;
  padding: 10px;
  box-shadow: 0 0 20px 5px rgba(182, 203, 8, 0.3);
}

button[type="submit"]:active {
  transform: scale(90%);
  box-shadow: 0 0 0px 0px rgba(183, 203, 81, 0.3);
}
</style>
