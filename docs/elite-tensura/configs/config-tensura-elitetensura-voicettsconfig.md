# `config/tensura/EliteTensura/VoiceTtsConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Tts]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | false |  | Master TTS switch. When false, no speech is produced; the overlay + level-up sound still work. |
| `provider` | "LOCAL" |  | TTS provider: ELEVENLABS \| GOOGLE \| LOCAL. LOCAL uses the client's Minecraft narrator (no key, no cost). Unknown values fall back to LOCAL. |
| `volume` | 1 |  | Playback volume for ELEVENLABS/GOOGLE audio, applied client-side. 0.0 - 1.0. (LOCAL narrator ignores this.) |
| `elevenlabsApiKey` | "" |  | ElevenLabs API key. Blank = ElevenLabs disabled. |
| `elevenlabsVoiceId` | "" |  | ElevenLabs voice id. |
| `googleApiKey` | "" |  | Google Cloud TTS API key. Blank = Google disabled. |
| `maxCharsPerCall` | 300 |  | Max characters sent to a paid provider per call. Longer text is truncated. &lt;= 0 disables the cap. (Does not limit LOCAL narration.) |
| `perPlayerCooldownSeconds` | 10 |  | Minimum seconds between TTS calls for the same player. Throttles spam and paid-API cost. |
| `allowPlayerTriggers` | false |  | Reserved: when false, only server-side events may trigger TTS, never raw player actions. Enforced once player-triggered events route through TtsManager. |
| `ttsNotice` | true |  | Speak NOTICE-tier Voice messages. |
| `ttsAnnouncement` | true |  | Speak ANNOUNCEMENT-tier Voice messages. |
| `ttsWarning` | true |  | Speak WARNING-tier Voice messages. |
| `ttsEvolution` | true |  | Speak EVOLUTION-tier Voice messages. |
| `ttsAchievement` | true |  | Speak ACHIEVEMENT-tier Voice messages. |
| `ttsError` | true |  | Speak ERROR-tier Voice messages. |
| `ttsSystem` | true |  | Speak SYSTEM-tier Voice messages. |
| `debug` | false |  | Log TTS routing decisions to the server console for debugging. |
