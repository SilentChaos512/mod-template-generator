package $PACKAGE$.init;

import $PACKAGE$.ExampleMod;
import net.minecraft.item.Item;
import net.minecraft.item.ItemBlock;
import net.minecraft.item.ItemGroup;
import net.minecraft.util.IItemProvider;
import net.minecraft.util.IStringSerializable;
import net.minecraft.util.ResourceLocation;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.registries.ForgeRegistries;

import java.util.ArrayList;
import java.util.Collection;

public final class ModItems {
    public static Item example;

    static final Collection<ItemBlock> blocksToRegister = new ArrayList<>();

    private ModItems() {}

    public static void registerAll(RegistryEvent.Register<Item> event) {
        // Workaround for Forge event bus bug
        if (!event.getName().equals(ForgeRegistries.ITEMS.getRegistryName())) return;

        // Register block items first
        blocksToRegister.forEach(ForgeRegistries.ITEMS::register);

        // Then register your items here
        example = register("example_item", new Item(new Item.Builder()
                .group(ItemGroup.MATERIALS)));
    }

    private static <T extends Item> T register(String name, T item) {
        ResourceLocation id = new ResourceLocation($MOD_CLASS$.MOD_ID, name);
        item.setRegistryName(id);
        ForgeRegistries.ITEMS.register(item);
        return item;
    }

    private static <E extends Enum<E> & IItemProvider & IStringSerializable> void registerFromEnum(Class<E> enumClass) {
        for (E e : enumClass.getEnumConstants()) {
            register(e.getName(), e.asItem());
        }
    }
}
