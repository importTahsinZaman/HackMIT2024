import { Pressable, Text, SafeAreaView, View } from "react-native";
import { Link } from "expo-router";

export default function DaysRemaining() {
  return (
    <View className="w-[45%] bg-[#a074f5] shadow rounded-2xl h-[60%] flex items-center justify-center">
      <Text className="font-bold text-white text-lg">Day:</Text>

      <Text className="m-4 font-bold text-[26px] text-white bg-[#a074f5]">
        40/120
      </Text>
    </View>
  );
}
