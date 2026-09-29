# `config/nightmare/deals/deal_config.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `maxActiveDeals` | 50 |  | Maximum number of active deals a player can have. |
| `maxDealDistance` | 100 |  | Maximum distance in blocks for deal creation. |
| `maxContractTemplates` | 100 |  | Maximum number of contract templates to load from the deals directory. |
| `defaultDealDurationSeconds` | 0 |  | Default deal duration in seconds (0 = no expiry). |
| `maxStoredDealsPerPlayer` | 100 |  | Maximum number of stored (completed/expired) deals retained per player in world data. |
| `maxActiveDealsPerPlayer` | 50 |  | Maximum number of active deals tracked per player in world data. |
| `autoPurgeExpiredDeals` | true |  | Whether to automatically purge expired deals from world data after they expire. |
| `purgeCheckIntervalSeconds` | 3,600 |  | Interval in seconds between expired deal purge checks (0 = disabled). |
| `filePersistenceEnabled` | false |  | Enable file-based persistence (config/nightmare/deals/&lt;uuid&gt;/deal.json). Disabled by default; SavedData is the primary persistence mechanism. |
| `webhookEnabled` | false |  | Enable Discord webhook notifications for deal events (create, break, complete). |
| `webhookUrl` | "" |  | Discord webhook URL for deal event notifications. |
| `webhookLevel` | "MAJOR_ONLY" |  | Webhook notification level: ALL, MAJOR_ONLY (create/break), OFF. |
| `soulForfeitEnabled` | true |  | Whether soul forfeit is enabled when a deal is broken. |
| `soulForfeitGracePeriodSeconds` | 300 |  | Grace period in seconds before soul forfeit takes effect after deal break. |
| `debugLogging` | false |  | Enable verbose debug logging for deal operations. |
