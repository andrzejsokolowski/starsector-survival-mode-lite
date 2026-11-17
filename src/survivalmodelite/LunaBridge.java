package survivalmodelite;

import com.fs.starfarer.api.Global;
import lunalib.lunaSettings.LunaSettings;
import lunalib.lunaSettings.LunaSettingsListener;

/** The only class that names LunaLib. Loaded only when LunaLib is enabled. */
final class LunaBridge implements LunaSettingsListener {

    private LunaBridge() {
    }

    static void listen() {
        LunaSettings.addSettingsListener(new LunaBridge());
    }

    static Double number(String id) {
        return LunaSettings.getDouble(SurvivalModeLitePlugin.MOD_ID, id);
    }

    static Integer integer(String id) {
        return LunaSettings.getInt(SurvivalModeLitePlugin.MOD_ID, id);
    }

    static Boolean bool(String id) {
        return LunaSettings.getBoolean(SurvivalModeLitePlugin.MOD_ID, id);
    }

    @Override
    public void settingsChanged(String modId) {
        if (!SurvivalModeLitePlugin.MOD_ID.equals(modId)) return;
        try {
            SurvivalModeLitePlugin.apply();
        } catch (Throwable t) {
            Global.getLogger(LunaBridge.class).error("Survival Mode - Lite: could not apply LunaLib settings", t);
        }
    }
}
