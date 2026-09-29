# Pack config overrides

Put copies of the modpack's config folders here to turn on **Pack notes**:

```
pack/
  config/          <- the instance's config/ folder
  defaultconfigs/  <- optional, if the pack ships one
```

Then run the render step (`python -m tools.wikigen.render ...`), or just push: the website workflow re-renders on every push to `main`. Any value that differs from a mod's default is marked on the matching page, in the config tables, and on the Pack notes page.
