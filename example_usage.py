from client import AgentFileSharingVirtualWorkspaceDriveClient

def main():
    client = AgentFileSharingVirtualWorkspaceDriveClient()
    res = client.store_and_share_artifact("dataset_analysis.parquet")
    print(f"Storage URI: {res['storage_uri']}")
    print(f"Share Status: {res['share_status']}")

if __name__ == "__main__":
    main()
