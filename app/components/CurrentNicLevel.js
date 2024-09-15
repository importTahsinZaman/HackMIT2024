import { Text, View } from "react-native";

export default function CurrentNicLevel({ data }) {
  return (
    <View className="bg-[#ff5c91] shadow rounded-2xl h-[60%] w-[45%] flex items-center justify-center">
      <Text className="font-bold text-white text-lg">Nicotine Dosage:</Text>

      <Text className="my-4 font-bold text-[26px] text-white">
        {data * 60 < 1 ? (data * 60).toFixed(2) : 0.54}mg/hour
      </Text>
    </View>
  );
}
