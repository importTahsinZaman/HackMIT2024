import AsyncStorage from "@react-native-async-storage/async-storage";
import { createClient } from "@supabase/supabase-js";

const supabaseUrl = "https://thubgzodxizmmtyvcfgp.supabase.co";
const supabaseAnonKey =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRodWJnem9keGl6bW10eXZjZmdwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjYzNDQ0NjUsImV4cCI6MjA0MTkyMDQ2NX0.kOBtx9MYpeKu4FV4wcfjet0mDpqwJmTGDwkTa4oVmP8";

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    storage: AsyncStorage,
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: false,
  },
});
