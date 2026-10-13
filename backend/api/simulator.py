from fastapi import APIRouter
from pydantic import BaseModel
from market_mind_ai.agents.scenario_agent import ScenarioAgent
from market_mind_ai.models.agent_schemas import ScenarioImpactOutput

router = APIRouter(prefix="/simulator", tags=["Macro Scenario Simulator"])

scenario_agent = ScenarioAgent()

class ScenarioQueryRequest(BaseModel):
    query: str

@router.post("/scenario", response_model=ScenarioImpactOutput)
def simulate_macro_scenario(req: ScenarioQueryRequest):
    return scenario_agent.analyze(req.query)
