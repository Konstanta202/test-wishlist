<script>
  export let checked = false;
  export let label = '';

  const handleToggle = (event) => {
    if (event.type === 'keydown' && ![' ', 'Enter'].includes(event.key)) return;

    checked = !checked;
    const evt = new CustomEvent('change', { detail: checked });
    dispatchEvent(evt);
  };
</script>

<button
  type="button"
  class="toggle"
  role="switch"
  aria-checked={checked}
  on:click={handleToggle}
  on:keydown={handleToggle}
>
  <div class="toggle-main">
    <div class="toggle-label">{label}</div>
  </div>
  <div class={`switch ${checked ? 'on' : ''}`}>
    <div class="thumb"></div>
  </div>
</button>

<style>
  .toggle {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    padding: 8px 0;
    cursor: pointer;
    border: none;
    background: transparent;
    width: 100%;
  }
  .toggle:focus-visible {
    outline: 2px solid #2563eb;
    outline-offset: 2px;
  }
  .toggle-label {
    font-size: 15px;
    text-align: left;
  }
  .switch {
    width: 44px;
    height: 26px;
    border-radius: 999px;
    background: #e5e7eb;
    padding: 2px;
    display: flex;
    align-items: center;
    transition: background 120ms ease, justify-content 120ms ease;
  }
  .switch.on {
    background: #2563eb;
    justify-content: flex-end;
  }
  .thumb {
    width: 22px;
    height: 22px;
    border-radius: 999px;
    background: #ffffff;
    box-shadow: 0 1px 4px rgba(15, 23, 42, 0.3);
  }
</style>
