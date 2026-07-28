---
hide:
  - toc
  - navigation
---

<div class="guide-hero">
  <p class="guide-hero__eyebrow">Getting Started · Step 4 of 5</p>
  <h1>Widget Setup</h1>
  <p class="guide-hero__summary">Build the Discord profile widget and connect every visual element to the exact User Data variable that WoWidget updates.</p>
  <div class="guide-meta"><span>⏱ 12–18 minutes</span><span>Exact configuration required</span></div>
</div>

<nav class="setup-progress" aria-label="Setup progress">
  <ol>
    <li class="is-complete"><a href="../installation/" data-step="1"><span class="setup-progress__marker" data-step="1" aria-hidden="true"></span><span class="setup-progress__label">Installation</span></a></li>
    <li class="is-complete"><a href="../blizzard-setup/" data-step="2"><span class="setup-progress__marker" data-step="2" aria-hidden="true"></span><span class="setup-progress__label">Blizzard</span></a></li>
    <li class="is-complete"><a href="../discord-setup/" data-step="3"><span class="setup-progress__marker" data-step="3" aria-hidden="true"></span><span class="setup-progress__label">Discord</span></a></li>
    <li class="is-current" aria-current="step"><a href="../widget-editor/" data-step="4"><span class="setup-progress__marker" data-step="4" aria-hidden="true"></span><span class="setup-progress__label">Widget</span></a></li>
    <li><a href="../application-setup/" data-step="5"><span class="setup-progress__marker" data-step="5" aria-hidden="true"></span><span class="setup-progress__label">Application</span></a></li>
  </ol>
</nav>

<section class="guide-panel">
  <h2>Before you begin</h2>
  <p>Open your Discord application and select <strong>Widget</strong> from the Games section. If the Widget tab is missing, repeat <a href="../discord-setup/">Discord Setup, Step 6</a>.</p>
</section>

<section class="guide-step guide-step--split">
  <div class="guide-step__copy">
    <div class="guide-step__heading"><span class="step-number">1</span><h2>Create the widget</h2></div>
    <p>Select <strong>Create Widget</strong>.</p>
  </div>
  <figure class="doc-screenshot">
    <img src="../../assets/images/widget/00-create-widget.png" alt="Discord Widget page Create Widget button" loading="lazy">
    <figcaption>Open the Widget section and create a new widget.</figcaption>
  </figure>
</section>

<section class="guide-step">
  <div class="guide-step__heading"><span class="step-number">2</span><h2>Configure Widget Top</h2></div>
  <p>Choose <strong>Widget Top</strong> from the dropdown, select the <strong>Hero</strong> layout, and open the <strong>Content</strong> tab. Hero gives the character model more room and blends it into the widget more naturally than Contained.</p>
  <div class="screenshot-gallery screenshot-gallery--3">
    <figure class="doc-screenshot"><img src="../../assets/images/widget/01-widget-top.png" alt="Discord Widget Editor Widget Top selector" loading="lazy"><figcaption>Select Widget Top.</figcaption></figure>
    <figure class="doc-screenshot"><img src="../../assets/images/widget/02-hero-layout.png" alt="Discord Widget Editor Hero layout option" loading="lazy"><figcaption>Choose Hero layout.</figcaption></figure>
    <figure class="doc-screenshot"><img src="../../assets/images/widget/03-content-tab.png" alt="Discord Widget Editor Content tab" loading="lazy"><figcaption>Open the Content tab.</figcaption></figure>
  </div>

  <aside class="ww-callout ww-callout--danger"><strong>Match every field exactly</strong><span>A misspelled Data Field, incorrect Value Type, or incorrect fallback can prevent an element from updating.</span></aside>

  <div class="config-pair">
    <section class="config-card">
      <header><h3>1 · Image</h3><span>Image</span></header>
      <table class="config-table"><tbody>
        <tr><th>Value Type</th><td>User Data</td></tr>
        <tr><th>Data Field</th><td><code>character_model</code></td></tr>
        <tr><th>Fallback</th><td>Disabled</td></tr>
      </tbody></table>
    </section>
    <section class="config-card">
      <header><h3>2 · Title</h3><span>Text</span></header>
      <table class="config-table"><tbody>
        <tr><th>Presentation Type</th><td>Text</td></tr>
        <tr><th>Value Type</th><td>User Data</td></tr>
        <tr><th>Data Field</th><td><code>character_name</code></td></tr>
        <tr><th>Fallback</th><td>Disabled</td></tr>
      </tbody></table>
    </section>
  </div>

  <section class="config-card config-card--full">
    <header><h3>3 · Subtitle 1</h3><span>Text + Icon</span></header>
    <table class="config-table config-table--four"><tbody>
      <tr><th>Label</th><td>Disabled</td><th>Presentation Type</th><td>Text</td></tr>
      <tr><th>Value Type</th><td>User Data</td><th>Data Field</th><td><code>race_class</code></td></tr>
      <tr><th>Fallback</th><td>Disabled</td><th>Icon</th><td>Enabled</td></tr>
      <tr><th>Icon Value Type</th><td>User Data</td><th>Icon Data Field</th><td><code>faction_icon</code></td></tr>
    </tbody></table>
  </section>

  <section class="config-card config-card--full">
    <header><h3>4 · Subtitle 2</h3><span>Label + Text</span></header>
    <table class="config-table config-table--four"><tbody>
      <tr><th>Label</th><td>Enabled</td><th>Label Value Type</th><td>Custom String</td></tr>
      <tr><th>Label Content</th><td>Realm</td><th>Presentation Type</th><td>Text</td></tr>
      <tr><th>Value Type</th><td>User Data</td><th>Data Field</th><td><code>realm</code></td></tr>
      <tr><th>Fallback</th><td>Disabled</td><th>Icon</th><td>Disabled</td></tr>
    </tbody></table>
  </section>

  <section class="config-card config-card--full">
    <header><h3>5 · Subtitle 3</h3><span>Label + Text</span></header>
    <table class="config-table config-table--four"><tbody>
      <tr><th>Label</th><td>Enabled</td><th>Label Value Type</th><td>Custom String</td></tr>
      <tr><th>Label Content</th><td>Guild</td><th>Presentation Type</th><td>Text</td></tr>
      <tr><th>Value Type</th><td>User Data</td><th>Data Field</th><td><code>guild</code></td></tr>
      <tr><th>Fallback</th><td>Enabled — <code>N/A</code></td><th>Icon</th><td>Disabled</td></tr>
    </tbody></table>
  </section>
</section>

<section class="guide-step">
  <div class="guide-step__heading"><span class="step-number">3</span><h2>Configure Widget Bottom</h2></div>
  <p>Choose <strong>Widget Bottom</strong>, select the <strong>Stats Grid</strong> layout, and open the <strong>Content</strong> tab. Stat 1 is recommended to be your current spec; slots 2–6 can use any five variables from the table below.</p>
  <div class="screenshot-gallery screenshot-gallery--2">
    <figure class="doc-screenshot"><img src="../../assets/images/widget/04-widget-bottom.png" alt="Discord Widget Editor Widget Bottom selector" loading="lazy"><figcaption>Select Widget Bottom, and choose Stats Grid.</figcaption></figure>
    <figure class="doc-screenshot"><img src="../../assets/images/widget/05-stats-grid.png" alt="Discord Widget Editor Stats Grid layout" loading="lazy"><figcaption>Open Content and input your chosen stats.</figcaption></figure>
  </div>

  <section class="config-card config-card--full">
    <header><h3>Stat 1 · Current Spec</h3><span>Required</span></header>
    <table class="config-table config-table--four"><tbody>
      <tr><th>Presentation Type</th><td>Text</td><th>Value Type</th><td>User Data</td></tr>
      <tr><th>Data Field</th><td><code>spec_name</code></td><th>Fallback</th><td>Disabled</td></tr>
      <tr><th>Label</th><td>Enabled</td><th>Label Value Type</th><td>Custom String</td></tr>
      <tr><th>Label Content</th><td>Current Spec</td><th>Icon</th><td>Enabled</td></tr>
      <tr><th>Icon Value Type</th><td>User Data</td><th>Icon Data Field</th><td><code>spec_icon</code></td></tr>
    </tbody></table>
  </section>

  <div class="section-heading"><div><p class="section-heading__eyebrow">Stats 2–6</p><h3>Choose five optional variables</h3></div><p>Match both the Presentation Type and Data Field exactly.</p></div>

  <div class="variable-guide-link">
    <div>
      <span class="variable-guide-link__eyebrow">Complete reference</span>
      <h3>Browse all Widget Variables</h3>
      <p>Open the categorized variable reference in a new tab, copy the five Data Fields you want to use, then return here to finish the Stats Grid.</p>
    </div>
    <a class="md-button md-button--primary" href="../../reference/widget-variables/" target="_blank" rel="noopener">Browse Widget Variables</a>
  </div>

  <aside class="ww-callout ww-callout--tip"><strong>These slots remain editable</strong><span>You can return to the Widget Editor later and change which five optional statistics appear.</span></aside>
</section>

<section class="guide-step">
  <div class="guide-step__heading"><span class="step-number">4</span><h2>Add Widget Preview</h2></div>
  <p>Choose <strong>Add Widget Preview</strong>, select the <strong>Hero</strong> layout, and configure Image using the same <code>character_model</code> User Data variable used in Widget Top.</p>
  <div class="screenshot-gallery screenshot-gallery--2">
    <figure class="doc-screenshot"><img src="../../assets/images/widget/06-add-widget-preview.png" alt="Discord Widget Editor Add Widget Preview option" loading="lazy"><figcaption>Add the required profile preview.</figcaption></figure>
    <figure class="doc-screenshot"><img src="../../assets/images/widget/07-preview-image.png" alt="Discord Widget Preview image configuration" loading="lazy"><figcaption>Use <code>character_model</code> for the Hero preview image.</figcaption></figure>
  </div>
  <aside class="ww-callout ww-callout--danger"><strong>Do not skip Widget Preview</strong><span>Discord requires a preview before the widget can be added to your profile.</span></aside>
</section>

<section class="guide-step guide-step--split">
  <div class="guide-step__copy">
    <div class="guide-step__heading"><span class="step-number">5</span><h2>Configure Mini Profile <small>(optional)</small></h2></div>
    <p>Enable the compact widget shown on your profile card in servers. The recommended setup is your character name as the stat, either <code>faction_icon</code> or <code>spec_icon</code> as the icon, and <code>character_model</code> as the image.</p>
  </div>
  <figure class="doc-screenshot"><img src="../../assets/images/widget/08-mini-profile.png" alt="Discord Widget Editor Mini Profile configuration" loading="lazy"><figcaption>Optionally configure the compact profile-card version.</figcaption></figure>
</section>

<section class="guide-step guide-step--split">
  <div class="guide-step__copy">
    <div class="guide-step__heading"><span class="step-number">6</span><h2>Save and publish</h2></div>
    <p>Select <strong>Save Changes</strong> in the upper-right corner, then select <strong>Publish</strong>.</p>
    <aside class="ww-callout ww-callout--success"><strong>Widget Editor complete</strong><span>Your widget structure is published. WoWidget can populate it after the final application setup.</span></aside>
  </div>
  <figure class="doc-screenshot"><img src="../../assets/images/widget/09-save-publish.png" alt="Discord Widget Editor Save Changes and Publish controls" loading="lazy"><figcaption>Save the configuration, then publish the widget.</figcaption></figure>
</section>

!!! tip "Enable Developer Mode"
    If you followed these steps and still can't add the widget to your Discord profile, make sure you have Devloper Mode enabled in your discord settings. Because these features are considered 'Experimental', the developer mode must be enabled to use them.  

