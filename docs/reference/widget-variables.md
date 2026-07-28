---
hide:
  - toc
  - navigation
---

<div class="guide-hero reference-hero">
  <p class="guide-hero__eyebrow">Discord User Data</p>
  <h1>Widget Variables</h1>
  <p class="guide-hero__summary">A complete reference for the user-data fields used by WoWidget and Discord's Widget Editor.</p>
  <div class="guide-meta"><span>Text, number, duration, and image fields</span><span>Names are case-sensitive</span></div>
</div>

<div class="variable-reference-intro">
  <div>
    <span class="variable-reference-intro__icon">{ }</span>
    <p><strong>Match every field exactly.</strong><br>Discord connects a widget element to WoWidget by its Data Field name and Presentation Type. A spelling or type mismatch prevents the value from appearing.</p>
  </div>
  <a class="md-button" href="../../getting-started/widget-editor/">Open Widget Editor guide</a>
</div>

<section class="reference-section">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Widget Top</p><h2>Identity and hero fields</h2></div>
    <p>These fields build the main character area of the widget.</p>
  </div>

  <div class="variable-card-grid">
    <article class="variable-card variable-card--image">
      <header><div class="variable-card__field"><code>character_model</code><button class="copy-button copy-button--compact" data-copy="character_model" aria-label="Copy character_model">Copy</button></div><span>Image</span></header>
      <h3>Character Portrait</h3>
      <p>The portrait saved in Portrait Studio and displayed in the Hero image area.</p>
      <footer>Recommended use: Widget Top image and Widget Preview</footer>
    </article>
    <article class="variable-card">
      <header><div class="variable-card__field"><code>character_name</code><button class="copy-button copy-button--compact" data-copy="character_name" aria-label="Copy character_name">Copy</button></div><span>Text</span></header>
      <h3>Character Name</h3>
      <p>The selected character's display name.</p>
      <footer>Recommended use: Title</footer>
    </article>
    <article class="variable-card">
      <header><div class="variable-card__field"><code>race_class</code><button class="copy-button copy-button--compact" data-copy="race_class" aria-label="Copy race_class">Copy</button></div><span>Text</span></header>
      <h3>Race and Class</h3>
      <p>A combined identity string such as “Blood Elf Demon Hunter.”</p>
      <footer>Recommended use: Subtitle 1</footer>
    </article>
    <article class="variable-card">
      <header><div class="variable-card__field"><code>realm</code><button class="copy-button copy-button--compact" data-copy="realm" aria-label="Copy realm">Copy</button></div><span>Text</span></header>
      <h3>Realm</h3>
      <p>The realm associated with the active character.</p>
      <footer>Recommended label: Realm:</footer>
    </article>
    <article class="variable-card">
      <header><div class="variable-card__field"><code>guild</code><button class="copy-button copy-button--compact" data-copy="guild" aria-label="Copy guild">Copy</button></div><span>Text</span></header>
      <h3>Guild Name</h3>
      <p>The character's current guild, or the application's fallback when no guild is returned.</p>
      <footer>Recommended label: Guild:</footer>
    </article>
    <article class="variable-card variable-card--image">
      <header><div class="variable-card__field"><code>faction_icon</code><button class="copy-button copy-button--compact" data-copy="faction_icon" aria-label="Copy faction_icon">Copy</button></div><span>Image</span></header>
      <h3>Faction Icon</h3>
      <p>The Alliance or Horde icon associated with the character.</p>
      <footer>Recommended use: Race/Class subtitle icon</footer>
    </article>
  </div>
</section>

<section class="reference-section">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Widget Bottom</p><h2>Required specialization fields</h2></div>
    <p>Use these together for the first Stats Grid slot.</p>
  </div>

  <div class="variable-card-grid variable-card-grid--compact">
    <article class="variable-card">
      <header><div class="variable-card__field"><code>spec_name</code><button class="copy-button copy-button--compact" data-copy="spec_name" aria-label="Copy spec_name">Copy</button></div><span>Text</span></header>
      <h3>Current Specialization</h3>
      <p>The active specialization name used as the first stat value.</p>
      <footer>Recommended label: Current Spec</footer>
    </article>
    <article class="variable-card variable-card--image">
      <header><div class="variable-card__field"><code>spec_icon</code><button class="copy-button copy-button--compact" data-copy="spec_icon" aria-label="Copy spec_icon">Copy</button></div><span>Image</span></header>
      <h3>Specialization Icon</h3>
      <p>The icon corresponding to the active character specialization.</p>
      <footer>Recommended use: Stat 1 icon</footer>
    </article>
  </div>
</section>

<section class="reference-section variable-reference-directory">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Stats 2–6</p><h2>Optional statistics</h2></div>
    <p>Choose any five fields supported by your current WoWidget build.</p>
  </div>
  <p class="variable-copy-tip">Select <strong>Copy</strong> beside any Data Field to place its exact value on your clipboard.</p>
  <nav class="variable-category-nav" aria-label="Widget variable categories">
    <a href="#character-statistics">Character</a>
    <a href="#progression-statistics">Progression</a>
    <a href="#pvp-statistics">PvP</a>
    <a href="#collection-statistics">Collections</a>
    <a href="#completion-statistics">Completion</a>
  </nav>
</section>

<section class="reference-section variable-category" id="character-statistics">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Optional statistics</p><h2>Character</h2></div>
    <p>General character and account activity fields.</p>
  </div>

  <div class="table-shell variable-reference-table-shell">
    <table class="variable-table variable-reference-table">
      <thead>
        <tr><th>Display name</th><th>Presentation type</th><th>Data field</th><th>Description</th></tr>
      </thead>
      <tbody>
        <tr><td>Character Level</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>character_level</code><button class="copy-button copy-button--compact" data-copy="character_level" aria-label="Copy character_level">Copy</button></div></td><td>Current character level.</td></tr>
        <tr><td>Last Logged In</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>last_login</code><button class="copy-button copy-button--compact" data-copy="last_login" aria-label="Copy last_login">Copy</button></div></td><td>Elapsed time since the character last logged in.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="reference-section variable-category" id="progression-statistics">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Optional statistics</p><h2>Progression</h2></div>
    <p>Core equipment, Mythic+, and raid progression fields.</p>
  </div>

  <div class="table-shell variable-reference-table-shell">
    <table class="variable-table variable-reference-table">
      <thead>
        <tr><th>Display name</th><th>Presentation type</th><th>Data field</th><th>Description</th></tr>
      </thead>
      <tbody>
        <tr><td>Item Level</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>gear_score</code><button class="copy-button copy-button--compact" data-copy="gear_score" aria-label="Copy gear_score">Copy</button></div></td><td>Current equipped item level.</td></tr>
        <tr><td>Mythic+ Rating</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>mythic_score</code><button class="copy-button copy-button--compact" data-copy="mythic_score" aria-label="Copy mythic_score">Copy</button></div></td><td>Current Mythic+ rating returned by Blizzard.</td></tr>
        <tr><td>Mythic+ Rating (Exact)</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>mythic_score2</code><button class="copy-button copy-button--compact" data-copy="mythic_score2" aria-label="Copy mythic_score2">Copy</button></div></td><td>Exact Mythic+ rating with thousands separators, such as <code>3,428</code>.</td></tr>
        <tr><td>Raid Progress</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>raid_score</code><button class="copy-button copy-button--compact" data-copy="raid_score" aria-label="Copy raid_score">Copy</button></div></td><td>Highest current-season progression, prioritizing Mythic, then Heroic, Normal, and Raid Finder.</td></tr>
        <tr><td>Heroic Raid Progress</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>heroic_score</code><button class="copy-button copy-button--compact" data-copy="heroic_score" aria-label="Copy heroic_score">Copy</button></div></td><td>Current-season Heroic progression only.</td></tr>
        <tr><td>Normal Raid Progress</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>normal_score</code><button class="copy-button copy-button--compact" data-copy="normal_score" aria-label="Copy normal_score">Copy</button></div></td><td>Current-season Normal progression only.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="reference-section variable-category" id="pvp-statistics">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Optional statistics</p><h2>PvP</h2></div>
    <p>Queue-specific ratings are sent as Text so Discord displays the complete value without abbreviation.</p>
  </div>

  <div class="table-shell variable-reference-table-shell">
    <table class="variable-table variable-reference-table">
      <thead>
        <tr><th>Display name</th><th>Presentation type</th><th>Data field</th><th>Description</th></tr>
      </thead>
      <tbody>
        <tr><td>Highest PvP Rating</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>pvp_score</code><button class="copy-button copy-button--compact" data-copy="pvp_score" aria-label="Copy pvp_score">Copy</button></div></td><td>Highest rating across every supported PvP queue and specialization.</td></tr>
        <tr><td>Solo Shuffle Rating</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>solo_score</code><button class="copy-button copy-button--compact" data-copy="solo_score" aria-label="Copy solo_score">Copy</button></div></td><td>Highest Solo Shuffle rating across all specializations.</td></tr>
        <tr><td>2v2 Arena Rating</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>two_score</code><button class="copy-button copy-button--compact" data-copy="two_score" aria-label="Copy two_score">Copy</button></div></td><td>Highest 2v2 Arena rating across all specializations.</td></tr>
        <tr><td>3v3 Arena Rating</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>three_score</code><button class="copy-button copy-button--compact" data-copy="three_score" aria-label="Copy three_score">Copy</button></div></td><td>Highest 3v3 Arena rating across all specializations.</td></tr>
        <tr><td>Battleground Blitz Rating</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>blitz_score</code><button class="copy-button copy-button--compact" data-copy="blitz_score" aria-label="Copy blitz_score">Copy</button></div></td><td>Highest Battleground Blitz rating across all specializations.</td></tr>
        <tr><td>Rated Battleground Rating</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>rbg_score</code><button class="copy-button copy-button--compact" data-copy="rbg_score" aria-label="Copy rbg_score">Copy</button></div></td><td>Highest Rated Battleground rating across all specializations.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="reference-section variable-category" id="collection-statistics">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Optional statistics</p><h2>Collections</h2></div>
    <p>Collection totals available for the selected character.</p>
  </div>

  <div class="table-shell variable-reference-table-shell">
    <table class="variable-table variable-reference-table">
      <thead>
        <tr><th>Display name</th><th>Presentation type</th><th>Data field</th><th>Description</th></tr>
      </thead>
      <tbody>
        <tr><td>Mounts</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>mount_score</code><button class="copy-button copy-button--compact" data-copy="mount_score" aria-label="Copy mount_score">Copy</button></div></td><td>Number of collected mounts.</td></tr>
        <tr><td>Pets</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>pet_score</code><button class="copy-button copy-button--compact" data-copy="pet_score" aria-label="Copy pet_score">Copy</button></div></td><td>Number of collected companion pets.</td></tr>
        <tr><td>Titles</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>title_score</code><button class="copy-button copy-button--compact" data-copy="title_score" aria-label="Copy title_score">Copy</button></div></td><td>Number of unlocked character titles.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="reference-section variable-category" id="completion-statistics">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Optional statistics</p><h2>Completion</h2></div>
    <p>Achievement and reputation completion fields.</p>
  </div>

  <div class="table-shell variable-reference-table-shell">
    <table class="variable-table variable-reference-table">
      <thead>
        <tr><th>Display name</th><th>Presentation type</th><th>Data field</th><th>Description</th></tr>
      </thead>
      <tbody>
        <tr><td>Achievements</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>a_score</code><button class="copy-button copy-button--compact" data-copy="a_score" aria-label="Copy a_score">Copy</button></div></td><td>Total achievement points.</td></tr>
        <tr><td>Achievements (Exact)</td><td><span class="type-chip type-chip--text">Text</span></td><td><div class="variable-copy"><code>a_score2</code><button class="copy-button copy-button--compact" data-copy="a_score2" aria-label="Copy a_score2">Copy</button></div></td><td>Exact achievement points with thousands separators, such as <code>27,345</code>.</td></tr>
        <tr><td>Achievements Icon</td><td><span class="type-chip">Image</span></td><td><div class="variable-copy"><code>a_icon</code><button class="copy-button copy-button--compact" data-copy="a_icon" aria-label="Copy a_icon">Copy</button></div></td><td>Achievement icon for use alongside either Achievements field.</td></tr>
        <tr><td>Feats of Strength</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>feats_score</code><button class="copy-button copy-button--compact" data-copy="feats_score" aria-label="Copy feats_score">Copy</button></div></td><td>Completed Feats of Strength.</td></tr>
        <tr><td>Exalted Reputations</td><td><span class="type-chip">Number</span></td><td><div class="variable-copy"><code>rep_score</code><button class="copy-button copy-button--compact" data-copy="rep_score" aria-label="Copy rep_score">Copy</button></div></td><td>Number of reputations at Exalted.</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="reference-section">
  <div class="section-heading">
    <div><p class="section-heading__eyebrow">Configuration rules</p><h2>Common field requirements</h2></div>
  </div>

  <div class="usage-action-grid">
    <article>
      <span>Names</span>
      <h3>Use exact Data Field values</h3>
      <p>Field names are case-sensitive. Do not add spaces, capitalization, or punctuation that is not shown in this reference.</p>
    </article>
    <article>
      <span>Types</span>
      <h3>Match the Presentation Type</h3>
      <p>A Number field must be configured as Number, an image field as Image, and <code>last_login</code> as Text.</p>
    </article>
    <article>
      <span>Publishing</span>
      <h3>Save and publish changes</h3>
      <p>After editing variables in Discord, select <strong>Save Changes</strong> and <strong>Publish</strong>, then run a WoWidget update.</p>
    </article>
  </div>
</section>

<aside class="ww-callout ww-callout--note"><strong>Available fields can evolve</strong><span>The variable set may expand as WoWidget adds new Blizzard data. Use the reference bundled with your current release when a field differs from an older screenshot or guide.</span></aside>
