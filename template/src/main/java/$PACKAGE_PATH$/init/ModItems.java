package $PACKAGE$.init;

import $PACKAGE$.$MOD_CLASS$;
import net.minecraft.item.Item;
import net.minecraft.item.ItemBlock;
import net.minecraft.item.ItemGroup;
import net.minecraft.util.ResourceLocation;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.registries.ForgeRegistries;

import java.util.LinkedHashMap;
import java.util.Map;

public final class ModItems {
    public static Item example;

    static final Map<String, ItemBlock> BLOCKS_TO_REGISTER = new LinkedHashMap<>();

    private ModItems() {}

    public static void registerAll(RegistryEvent.Register<Item> event) {
        // Workaround for Forge event bus bug
        if (!event.getName().equals(ForgeRegistries.ITEMS.getRegistryName())) return;

        // Register block items first
        BLOCKS_TO_REGISTER.forEach(ModItems::register);

        // Then register your items here
        example = register("example_item", new Item(new Item.Properties()
                .group(ItemGroup.MATERIALS)));
    }

    private static <T extends Item> T register(String name, T item) {
        ResourceLocation id = $MOD_CLASS$.getId(name);
        item.setRegistryName(id);
        ForgeRegistries.ITEMS.register(item);
        return item;
    }
}
