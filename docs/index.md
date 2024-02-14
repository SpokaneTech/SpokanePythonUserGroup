---
hide:
  - navigation
  - title
---

<!-- Hide H1, it's already shown in the navbar -->
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }

  #upcoming-meetups {
    margin-top: 0px;
  }

  /* Hide H3s and below */
  .md-nav__list > .md-nav__item > .md-nav > .md-nav__list > .md-nav__item > .md-nav {
    display: none;
  }
</style>

# Spokane Python User Group

<!-- <div class="callout">
  <p>
    🚨 We are looking for <a href="/speak/#submit-proposal">speakers to present</a> in 2023! 
  </p>
</div> -->

## Upcoming Meetups

{%
  include-markdown "meetups/rust-bindings.md"
  heading-offset=2
  start="<!-- index: start -->"
  end="<!-- index: end -->"
%}

---

{%
  include-markdown "coffee/spokane.md"
  heading-offset=2
%}

---

{%
  include-markdown "coffee/cda.md"
  heading-offset=2
%}

## Previous Meetups

You can find our previous meetups [here](meetups/spokane-tech-kick-off.md).
