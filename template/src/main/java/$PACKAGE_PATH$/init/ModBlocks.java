package $PACKAGE$.init;

import $PACKAGE$.$MOD_CLASS$;
import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import net.minecraft.item.Item;
import net.minecraft.item.ItemBlock;
import net.minecraft.item.ItemGroup;
import net.minecraft.util.ResourceLocation;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.registries.ForgeRegistries;

public final class ModBlocks {
    public static Block example;

    private ModBlocks() {}

    public static void registerAll(RegistryEvent.Register<Block> event) {
        // Workaround for Forge event bus bug
        if (!event.getName().equals(ForgeRegistries.BLOCKS.getRegistryName())) return;

        // Register your blocks here
        example = register("example_block", new Block(Block.Builder
                .create(Material.ROCK)
                .hardnessAndResistance(4, 20)));
    }

    private static <T extends Block> T register(String name, T block) {
        ItemBlock item = new ItemBlock(block, new Item.Builder()
                .group(ItemGroup.BUILDING_BLOCKS));
        return register(name, block, item);
    }

    private static <T extends Block> T register(String name, T block, ItemBlock item) {
        ResourceLocation id = new ResourceLocation($MOD_CLASS$.MOD_ID, name);
        block.setRegistryName(id);
        ForgeRegistries.BLOCKS.register(block);

        item.setRegistryName(id);
        ModItems.blocksToRegister.add(item);

        return block;
    }
}
