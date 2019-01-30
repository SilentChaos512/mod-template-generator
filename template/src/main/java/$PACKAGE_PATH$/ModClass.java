package $PACKAGE$;

import net.minecraftforge.fml.DistExecutor;
import net.minecraftforge.fml.common.Mod;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Random;

@Mod($MOD_CLASS$.MOD_ID)
public final class $MOD_CLASS$ {
    public static final String MOD_ID = "$MOD_ID$";
    public static final String MOD_NAME = "$MOD_NAME$";
    public static final String RESOURCE_PREFIX = MOD_ID + ":";

    public static final Logger LOGGER = LogManager.getLogger(MOD_NAME);
    public static final Random RANDOM = new Random();

    public static $MOD_CLASS$ INSTANCE;
    public static SideProxy PROXY;

    public $MOD_CLASS$() {
        INSTANCE = this;
        PROXY = DistExecutor.runForDist(() -> () -> new SideProxy.Client(), () -> () -> new SideProxy.Server());
    }
}
