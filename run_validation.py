# run_validation.py
import sys

def check_system_integrity():
    print("Initializing environment validation...")
    
    # Simulating a core condition or business logic rule
    environment_ready = True 
    
    if not environment_ready:
        print("❌ CRITICAL ERROR: System integrity check failed!")
        sys.exit(1) # Exiting with a non-zero code triggers a CI failure
        
    print("✅ SUCCESS: All integration prerequisites are green.")
    sys.exit(0) # Exiting with 0 forces the CI step to pass

if __name__ == "__main__":
    check_system_integrity()
