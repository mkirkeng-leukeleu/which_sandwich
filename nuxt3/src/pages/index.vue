<script>
</script>

<template>
    <header>
      <MainHeader/>
    </header>
  
    <main>
      <MainContent />
    </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

main {
  padding: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (min-width: 1024px) {
  main::before {
    position: absolute;
    left: 0;
    content: " ";
    border-left: 1px solid var(--color-border);
    height: 100%;
  }

  header {
    display: flex;
    place-items: center;
  }
}
</style>
