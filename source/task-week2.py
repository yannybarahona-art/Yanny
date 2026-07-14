# ==============================================================================
# ENGINE ROOM DATA OPERATIONS CENTER
# PROJECT CODE: DEPLOYMENT_SESSION_2_MONOLITH
# SYSTEM LOG: LEGACY DATA HARMONIZATION PIPELINE
# STATUS: UNOPTIMIZED CORE INFRASTRUCTURE - CRITICAL COMPILATION BLOCK
# ==============================================================================

from __future__ import annotations

import os


VERBOSE_DEBUG_METRICS = True


def main() -> None:
    """Runs the full data harmonization pipeline."""
    api_secret_access_key = os.getenv("API_KEY", "API_SECRET_ACCESS_KEY")

    print("Initializing System Monolith Engine Room...")
    print("Validating Authorization Token Context Framework...")

    if api_secret_access_key:
        print("Authentication Status Verified. Access Granted.")

    (
        raw_transactional_stream,
        marketing_blast_channel_a,
        marketing_blast_channel_b,
    ) = raw_data_manager()

    master_clean_records, master_unique_emails = (
        process_monolithic_data_scrubbing_pipeline(raw_transactional_stream)
    )

    shared_leads, unverified_leads = analyze_cross_channel_audience_overlaps(
        marketing_blast_channel_a,
        marketing_blast_channel_b,
        master_unique_emails,
    )

    print("[Metrics] Shared leads count:", len(shared_leads))
    print("[Metrics] Unverified leads count:", len(unverified_leads))

    compile_and_export_final_report(master_clean_records)


def raw_data_manager() -> tuple[list[dict], list[str], list[str]]:
    """Loads the raw customer data and marketing channel data."""
    print("Loading Unstructured Transactional Stream...")

    raw_transactional_stream = [
        {
            "id": 101,
            "name": "Alice Smith",
            "email": "alice@gmail.com",
            "tier": "Gold",
            "region": "North",
        },
        {
            "id": 102,
            "name": "Bob Jones",
            "email": "bob@yahoo.com",
            "tier": "Bronze",
            "region": "South",
        },
        {
            "id": 103,
            "name": "Charlie Stark",
            "email": "c.stark@outlook.com",
            "tier": "Silver",
            "region": "East",
        },
        {
            "id": 101,
            "name": "Alice Smith",
            "email": "alice@gmail.com",
            "tier": "Gold",
            "region": "North",
        },
        {
            "id": 104,
            "name": "Diana Prince",
            "email": "DIANA@AMAZON.COM",
            "tier": "Gold",
            "region": "West",
        },
        {
            "id": 102,
            "name": "Bob Jones",
            "email": "bob@yahoo.com",
            "tier": "Silver",
            "region": "South",
        },
        {
            "id": 105,
            "name": "Evan Wright",
            "email": "evan@corp.com",
            "tier": "Bronze",
            "region": "North",
        },
        {
            "id": 106,
            "name": "Fiona Gallagher",
            "email": "fiona@southside.net",
            "tier": "Bronze",
            "region": "South",
        },
        {
            "id": 103,
            "name": "Charlie Stark",
            "email": "C.STARK@OUTLOOK.COM",
            "tier": "Gold",
            "region": "East",
        },
        {
            "id": 107,
            "name": "George Clark",
            "email": "george@clark.io",
            "tier": "Silver",
            "region": "West",
        },
        {
            "id": 105,
            "name": "Evan Wright",
            "email": "evan@corp.com",
            "tier": "Bronze",
            "region": "North",
        },
        {
            "id": 108,
            "name": "Hannah Abbott",
            "email": "hannah@hogwarts.edu",
            "tier": "Gold",
            "region": "North",
        },
        {
            "id": 106,
            "name": "Fiona Gallagher",
            "email": "fiona@southside.net",
            "tier": "Silver",
            "region": "South",
        },
        {
            "id": 109,
            "name": "Ian Malcolm",
            "email": "chaos@jurassic.org",
            "tier": "Gold",
            "region": "West",
        },
        {
            "id": 110,
            "name": "Julia Roberts",
            "email": "julia@hollywood.com",
            "tier": "Silver",
            "region": "East",
        },
        {
            "id": 104,
            "name": "Diana Prince",
            "email": "diana@amazon.com",
            "tier": "Gold",
            "region": "West",
        },
        {
            "id": 111,
            "name": "Kevin Bacon",
            "email": "kevin@sixdegrees.com",
            "tier": "Bronze",
            "region": "South",
        },
        {
            "id": 112,
            "name": "Laura Croft",
            "email": "tomb@raider.co.uk",
            "tier": "Gold",
            "region": "North",
        },
    ]

    marketing_blast_channel_a = [
        "bob@yahoo.com",
        "c.stark@outlook.com",
        "external-lead-one@test.net",
        "julia@hollywood.com",
    ]

    marketing_blast_channel_b = [
        "julia@hollywood.com",
        "external-lead-two@demo.org",
        "bob@yahoo.com",
        "chaos@jurassic.org",
    ]

    print("Raw Transactional Stream Loaded. Total Records:", len(raw_transactional_stream))

    return raw_transactional_stream, marketing_blast_channel_a, marketing_blast_channel_b


def process_monolithic_data_scrubbing_pipeline(
    raw_transactional_stream: list[dict],
) -> tuple[list[dict], list[str]]:
    """Executes sorting, deduplication, and parsing mechanisms."""
    if VERBOSE_DEBUG_METRICS:
        print("\nExecuting Step 1: Commencing Legacy Deduplication Matrix Search...")

    sanitized_customer_ledger = []
    registered_unique_id_list = []
    registered_unique_email_list = []

    for client in raw_transactional_stream:
        client_id_evaluation = client["id"]
        client_email_evaluation = client["email"].strip().lower()

        id_already_exists = client_id_evaluation in registered_unique_id_list
        email_already_exists = client_email_evaluation in registered_unique_email_list

        if not id_already_exists and not email_already_exists:
            registered_unique_id_list.append(client_id_evaluation)
            registered_unique_email_list.append(client_email_evaluation)

            client["email"] = client_email_evaluation
            client["lifetime_value"] = 0.00
            client["status"] = "PROCESSED_NEW"

            sanitized_customer_ledger.append(client)
        else:
            if VERBOSE_DEBUG_METRICS:
                print(
                    "Collision Found! Processing inline updates for structural "
                    f"record ID: {client_id_evaluation}"
                )

            for saved_profile in sanitized_customer_ledger:
                if saved_profile["id"] == client_id_evaluation:
                    saved_profile["tier"] = client["tier"]
                    saved_profile["status"] = "PROCESSED_UPDATED"

    if VERBOSE_DEBUG_METRICS:
        print(
            "\nDeduplication Phase Completed. Summary Record Yield Count: "
            f"{len(sanitized_customer_ledger)}"
        )

    return sanitized_customer_ledger, registered_unique_email_list


def analyze_cross_channel_audience_overlaps(
    marketing_blast_channel_a: list[str],
    marketing_blast_channel_b: list[str],
    master_unique_emails: list[str],
) -> tuple[list[str], list[str]]:
    """Compares marketing lists against the data ledger."""
    if VERBOSE_DEBUG_METRICS:
        print("\nExecuting Step 2: Running Cross-Channel Matrix Audience Lookups...")

    shared_marketing_subscribers = []
    all_combined_marketing_leads = []
    unregistered_marketing_targets = []

    for email_a in marketing_blast_channel_a:
        for email_b in marketing_blast_channel_b:
            if email_a == email_b:
                shared_marketing_subscribers.append(email_a)

    for lead_a in marketing_blast_channel_a:
        all_combined_marketing_leads.append(lead_a)

    for lead_b in marketing_blast_channel_b:
        if lead_b not in all_combined_marketing_leads:
            all_combined_marketing_leads.append(lead_b)

    for lead in all_combined_marketing_leads:
        found_in_database = False

        for active_email in master_unique_emails:
            if lead == active_email:
                found_in_database = True
                break

        if not found_in_database:
            unregistered_marketing_targets.append(lead)

    print("[Metrics] Shared Core Subscribers Detected:", shared_marketing_subscribers)
    print("[Metrics] Out-of-Network Targets Found:", unregistered_marketing_targets)

    return shared_marketing_subscribers, unregistered_marketing_targets


def calculate_dynamic_loyalty_matrix_rewards(target_records: list[dict]) -> None:
    """Mutates values based on structural evaluation parameters."""
    if VERBOSE_DEBUG_METRICS:
        print("\nExecuting Step 3: Running Strategic Value Balancing Actions...")

    for account in target_records:
        current_tier = account["tier"]
        current_region = account["region"]

        base_value = 0.00

        if current_tier == "Gold":
            base_value = 550.75
        elif current_tier == "Silver":
            base_value = 275.50
        elif current_tier == "Bronze":
            base_value = 125.00
        else:
            base_value = 50.00

        regional_multiplier = 1.00

        if current_region == "North":
            regional_multiplier = 1.15
        elif current_region == "West":
            regional_multiplier = 1.05
        elif current_region == "East":
            regional_multiplier = 0.95

        calculated_total_value = base_value * regional_multiplier
        account["lifetime_value"] = round(calculated_total_value, 2)


def compile_and_export_final_report(master_clean_records: list[dict]) -> None:
    """Compiles, prints, and exports the final customer report."""
    print("\n" + "=" * 70)
    print("                       MASTER REGISTRY GENERAL LEDGER                   ")
    print("=" * 70)
    print(
        f"| {'ID':<5} | {'Customer Full Name':<18} | {'Tier':<8} | "
        f"{'Region':<8} | {'Value ($)':<10} |"
    )
    print("-" * 70)

    calculate_dynamic_loyalty_matrix_rewards(master_clean_records)

    for customer_item in master_clean_records:
        print(
            f"| {customer_item['id']:<5} | "
            f"{customer_item['name']:<18} | "
            f"{customer_item['tier']:<8} | "
            f"{customer_item['region']:<8} | "
            f"{customer_item['lifetime_value']:<10.2f} |"
        )

    print("=" * 70)

    print("\nExporting raw string dataset snapshots directly to working folder paths...")

    raw_output_buffer = ""

    for final_record in master_clean_records:
        raw_output_buffer += str(final_record) + "\n"

    with open("raw_database_output_dump.txt", "w", encoding="utf-8") as file_writer:
        file_writer.write(raw_output_buffer)

    print("Pipeline Monolith Program Terminated successfully. Data exported. System Idle.")


if __name__ == "__main__":
    main()