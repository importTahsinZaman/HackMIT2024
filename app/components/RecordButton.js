import { Pressable, Text } from "react-native";
import { Link } from "expo-router";

export default function RecordButton() {
  return (
    <Link href="/TestScreen" asChild>
      <Pressable className="bg-green-400 rounded-full w-28 h-28 justify-center items-center">
        <Text className="font-bold text-lg">test</Text>
      </Pressable>
    </Link>
  );
}
