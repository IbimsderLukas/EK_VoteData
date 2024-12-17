import grpc
import vote_pb2
import vote_pb2_grpc
from concurrent import futures
import time


class VoteService(vote_pb2_grpc.VoteServiceServicer):
    def getVoteData(self, request, context):
        try:
            # Überprüfe, ob das Feld VoteId korrekt ist
            if not request.VoteId:
                context.set_details("Invalid vote_id field")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return vote_pb2.VoteResponse()

            # Ausgabe der empfangenen VoteId zur Überprüfung
            print(f"Received vote ID: {request.VoteId}")

            # Beispielantwort, normalerweise würdest du Daten aus einer Datenbank oder Logik ziehen
            response = vote_pb2.VoteResponse(
                VoteId=request.VoteId,
                candidates=[
                    vote_pb2.CandidateData(candidateName="Harald Hacker", votes=3000),
                    vote_pb2.CandidateData(candidateName="Sophie Schmidt", votes=2500)
                ]
            )

            # Sende die Antwort zurück
            return response
        except Exception as e:
            # Fehlerbehandlung und detaillierte Fehlermeldung zurück an den Client
            context.set_details(f"Error: {str(e)}")
            context.set_code(grpc.StatusCode.UNKNOWN)
            return vote_pb2.VoteResponse()


def serve():
    # Erstelle den Server und füge den Service hinzu
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vote_pb2_grpc.add_VoteServiceServicer_to_server(VoteService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server starting on port 50051...")

    # Starte den Server
    server.start()
    try:
        while True:
            time.sleep(86400)  # Server läuft weiter
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
