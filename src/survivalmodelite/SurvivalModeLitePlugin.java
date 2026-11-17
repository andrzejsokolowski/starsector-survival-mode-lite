package survivalmodelite;

import com.fs.starfarer.api.BaseModPlugin;
import com.fs.starfarer.api.Global;
import com.fs.starfarer.api.SettingsAPI;
import com.fs.starfarer.api.impl.campaign.Tuning;
import org.apache.log4j.Logger;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Without LunaLib the Lite values come from data/config/settings.json and this plugin does nothing.
 * With LunaLib it writes the player's values into the game's settings at application load and whenever
 * they change. The game reads these survival settings when it uses them (prices, drops, pay and so on),
 * so a change applies at once. The one exception is the threat slowdown, which the game copies into
 * Tuning.EXT_DELAY_FACTOR once; that field is set here too.
 */
public class SurvivalModeLitePlugin extends BaseModPlugin {

    static final String MOD_ID = "survival_mode_lite";
    static final String FIELDS = "data/config/survival_mode_lite_fields.json";
    private static final Logger log = Global.getLogger(SurvivalModeLitePlugin.class);

    @Override
    public void onApplicationLoad() {
        if (!Global.getSettings().getModManager().isModEnabled("lunalib")) {
            log.info("Survival Mode - Lite: LunaLib not enabled, using the Lite values from settings.json");
            return;
        }
        try {
            LunaBridge.listen();
            apply();
        } catch (Throwable t) {
            log.error("Survival Mode - Lite: could not read LunaLib settings, using the Lite values", t);
        }
    }

    /** Again on every game load, in case LunaLib had not read its settings file yet at application load. */
    @Override
    public void onGameLoad(boolean newGame) {
        if (!Global.getSettings().getModManager().isModEnabled("lunalib")) return;
        try {
            apply();
        } catch (Throwable t) {
            log.error("Survival Mode - Lite: could not apply LunaLib settings", t);
        }
    }

    /** Copies every LunaLib value into the game's settings. */
    static void apply() throws Exception {
        SettingsAPI settings = Global.getSettings();
        JSONArray fields = settings.loadJSON(FIELDS, MOD_ID).getJSONArray("fields");
        int applied = 0;
        for (int i = 0; i < fields.length(); i++) {
            JSONObject field = fields.getJSONObject(i);
            String id = field.getString("id");
            String key = field.getString("key");
            String unit = field.getString("unit");
            int index = field.optInt("index", -1);

            if ("bool".equals(unit)) {
                Boolean on = LunaBridge.bool(id);
                if (on == null) continue;
                settings.setBoolean(key, on);
                applied++;
                continue;
            }

            Double raw = "int".equals(unit) ? toDouble(LunaBridge.integer(id)) : LunaBridge.number(id);
            if (raw == null) continue;
            double value = "pct".equals(unit) || "per100".equals(unit) ? raw / 100.0 : raw;

            if (index >= 0) {
                // Lists are read live from the settings JSON, so changing the entry in place is enough.
                JSONArray list = settings.getSettingsJSON().getJSONArray(key);
                list.put(index, value);
            } else {
                settings.setFloat(key, (float) value);
            }
            if ("ext_timeBasedThingsDelayFactor".equals(key)) {
                Tuning.EXT_DELAY_FACTOR = (float) value;
            }
            applied++;
        }
        log.info("Survival Mode - Lite: applied " + applied + " LunaLib values");
    }

    private static Double toDouble(Integer value) {
        return value == null ? null : value.doubleValue();
    }
}
